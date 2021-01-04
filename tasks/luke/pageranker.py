import struct
import array
import sys
import numpy as np
from scipy.sparse import dok_matrix
from scipy.sparse import diags
from nltk.stem import PorterStemmer

class PageRanker(object):

    def __init__(self, 
                 titles_filename,
                 inverse_titles_index_filename,
                 word_index_filename,
                 links_filename):
        # read in the titles and word index
        # these methods swiped directly from Klein
        self.titles = PageRanker.read_titles(titles_filename)  
        self.word_index = PageRanker.read_word_index(word_index_filename)

        self.inverse_titles_index_filename = inverse_titles_index_filename
        self.links_filename = links_filename
        
        self.titles_index_map = {}

        print("Building map from title:position in vector")
        # first buiild a map from a title to its numeric position in the list of titles
        for i, val in enumerate(self.titles):
            self.titles_index_map[val] = i

        self.page_rank_vec = None
        self.pstem = PorterStemmer()

    @staticmethod
    def compute_pagerank_vector(page_ranker, power_iterations=20):
        # takes in a PageRanker instance and returns a pagerank vector
        #separated from PageRanker class so this can be run once separately

        # imports data, sets up sparse matrix, and computes eigenvector using power method
        if page_ranker.page_rank_vec is not None:
            print("already assigned a page_rank_vec")
            return

        print("Starting expensive set-up. This will take a bit.")

        # read in the wikipedia data and build the links matrix
        # this code borrows from Klein but builds a sparse matrix from his links map
        print("Reading in wikipedia data from {0}".format(page_ranker.links_filename))
        # len(self.titles)
        links_mat = dok_matrix((len(page_ranker.titles), len(page_ranker.titles)))
        links_set, links_map = PageRanker.generate_links(page_ranker.titles, page_ranker.links_filename)

        

        print("building full links matrix") 
        # now build out the sparse links matrix (1 if the row/col is linked, 0 otherwise)
        for link_pair in links_map.keys():
            row = page_ranker.titles_index_map[link_pair[0]]
            col = page_ranker.titles_index_map[link_pair[1]]
            links_mat[row, col] = 1

        print("Making links matrix markov...") 
        # we now have a links matrix with 1's in the corresponding cols/rows where a link exists
        # let's make this into a markov matrix
        markov_links_mat = PageRanker.make_markov(links_mat)

        print("Computing power method on our markov matrix to get our pagerank'd eigenvector")
        # now compute the power method to give us our pagerank eigenvector
        # note this method adds the 0.15 random noise
        final_output_vec =  PageRanker.power_method_sparse(markov_links_mat, power_iterations)        
        return final_output_vec

    def query(self, word, num_results=10):
        # first get the titles of pages containing the word
        title_indices = self.get_titles_for_word(word)

        # then get the values for those titles from the pagerank vector
        titles_and_values = []
        for idx in title_indices:
            titles_and_values.append((self.titles[idx], self.page_rank_vec[idx]))
        
        # then sort the list by rank and return it
        titles_and_values.sort(key=lambda x: x[1], reverse=True)
        return titles_and_values[0:num_results]
    
    def find_word(self, word):
        stem = self.pstem.stem(word)
        indices = self.get_titles_for_word(stem)
        return [self.titles[i] for i in indices] if indices else []

    def get_titles_for_word(self, word):
        _little_endian = (struct.unpack('<i', struct.pack('=i', 1))[0] == 1)
        ptr = self.word_index.get(word)
        if(ptr is None): return []
        with open(self.inverse_titles_index_filename, 'rb') as f:
            f.seek(ptr)
            nints = struct.unpack('>i', f.read(4))[0]
            arr = array.array("i")
            arr.fromfile(f, nints)
        if _little_endian:
            arr.byteswap()
        return arr.tolist()

    @staticmethod
    def read_titles(filename):
        with open(filename) as f:
            titles = [line.strip().replace(r'\n', '\n') for line in f]
        return titles

    @staticmethod
    def read_word_index(filename):
        with open(filename) as f:
            return dict((w.strip(), int(n)) for w,n in zip(f, f))

    @staticmethod
    def generate_links(titles, links_filename, verbose=True):
        _little_endian = (struct.unpack('<i', struct.pack('=i', 1))[0] == 1)
        Mf = {}
        with open(links_filename, 'rb') as f:
            for i, title in enumerate(titles):
                if verbose and (i%10000 == 9999):
                    print (".",end='')
                    sys.stdout.flush()
                nints = struct.unpack('<i', f.read(4))[0]
                arr = array.array('I')
                arr.fromfile(f, nints)
                if not _little_endian:
                    arr.byteswap()
                Mf.update(((title, titles[x]),1) for x in arr)
                # Link every page to itself, to avoid empty columns
                Mf[title,title] = 1
        if verbose: print()
        ts = set(titles)
        return ts,Mf

    @staticmethod
    def find_num_links(link_mat):
        # takes in a scipy sparse matrix
        # returns a vector equal in length to columns of link_mat
        # each row in the vector is the sum of links in the corresponding column
        ones_vec = np.ones(link_mat.shape[0])
        return link_mat.transpose().dot(ones_vec)
        
    @staticmethod    
    def make_markov(link_mat):
        num_links = PageRanker.find_num_links(link_mat)
        num_links_weights = 1/num_links    
        diag_mat = dok_matrix((link_mat.get_shape()[0], link_mat.get_shape()[0]))
        diag_mat.setdiag(num_links_weights)
        multiplied = link_mat@diag_mat
        return multiplied
    
    @staticmethod
    def power_method_sparse(markov_mat, num_iters, noise=0.15):
        markov_mat_weight = 1 - noise
        init_vec = np.full(markov_mat.get_shape()[1], 1)
        A2_val = 1/markov_mat.get_shape()[1]
        a2_vec = np.full(len(init_vec), A2_val)
        output_vec = init_vec
        for i in range(num_iters):
            w = markov_mat.dot(output_vec)
            a2_adjust = noise * output_vec.dot(a2_vec)
            output_vec = (.85*w) + a2_adjust
        return output_vec

