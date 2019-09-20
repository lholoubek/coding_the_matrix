from ch_1_the_field import plotting, image, png
import os

L = [[2,2],[3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75, 1], [3,1], [3.25,1]]

# task 2.3.2
def task_2_3_2():
    plotting.plot(L, 4)

# task 2.4.3
def add2(vector, update):
    return [vector[0] + update[0], vector[1] + update[1]]

def scale_vec(vector, scale):
    return [x*scale for x in vector]

def task_2_4_3():
    translation = [1,2]
    updated = [add2(item, translation) for item in L]
    plotting.plot(updated, 6)

# task 2.5.4
def vec_mult(vector, scalar):
    multiplied = [x*scalar for x in vector]
    return multiplied 

def task_2_5_4():
    plotting.plot(scale(L, 0.5), 5)
    plotting.plot(scale(L, -0.5), 5)

# task 2.6.9
def segment(pt1, pt2, factor):
    mid_pt1 = vec_mult(pt1, factor) 
    mid_pt2 = vec_mult(pt2, 1 - factor)
    scaled = add2(mid_pt1,mid_pt2)
    return scaled

def task_2_6_9():
    one_vec = [2,4]
    two_vec = [4,8]
    factors = [x/100 for x in range(100)]
    segmented_points = [segment([3.5,3], [0.5,1], x) for x in factors]
    print(segmented_points)
    plotting.plot(segmented_points, 10)


# Lab 2.12 - Comparing voting records
repo_path = os.path.expanduser("~") + "/Documents/coding_the_matrix"
voting_record_file = os.path.join(repo_path, "support", "ch_2","voting_record_dump109.txt")

class VotingRecords(object):
    def __init__(self, file_path):
        file = open(file_path)
        records = [x.split(' ') for x in file.readlines()]
        names = [x[0] for x in records]
        votes = [x[3:] for x in records]
        vote_vals = [[int(x) for x in vote_strings] for vote_strings in votes]
        self.voting_records = dict(zip(names, vote_vals))

    @staticmethod
    def dot(vec_a, vec_b):
        if len(vec_a) != len(vec_b):
            raise ValueError("Vectors are different lengths!")
        return sum([vec_a[x] * vec_b[x] for x in range(len(vec_a))])
    
    def check_records(self, *args):
        for sen in args:
            record = self.voting_records.get(sen)
            if not record:
                raise KeyError("Senator names not correct")
        return True

    # task 2.12.2
    def policy_compare(self, sen_a, sen_b):
        self.check_records(sen_a, sen_b)
        return self.dot(self.voting_records.get(sen_a), self.voting_records.get(sen_b))
    
    def print_senator_names(self):
        print(self.voting_records.keys())

def lab_main():
    voting_records = VotingRecords(voting_record_file)
    # voting_records.print_senator_names()
    print(voting_records.policy_compare('Obama', 'Grassley'))
    



if __name__ == "__main__":
    # task_2_3_2()
    # task_2_4_3()
    # task_2_5_4()
    # task_2_6_9()
    # print(voting_record_file)
    lab_main()