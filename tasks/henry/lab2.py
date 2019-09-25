#!/usr/bin/env python


def dot_product(a, b):
    assert isinstance(a, list)
    assert isinstance(b, list)
    assert len(a) == len(b)

    s = 0
    for i_a, i_b in zip(a, b):
        s += i_a*i_b
    return s

def vec_add(a, b):
    assert isinstance(a, list)
    assert isinstance(b, list)
    assert len(a) == len(b)

    result = []
    for i_a, i_b in zip(a, b):
        result.append(i_a + i_b)
    return result

def vec_div(a, alpha):
    result = []
    for i_a in a:
        result.append(i_a*1.0/alpha)
    return result

# Task 2.12.1
def create_voting_dict(strlist):
    d = {}
    for line in strlist:
        line = line.strip().split(' ')
        name = line[0]
        votes = [int(v) for v in line[3:]]
        d[name] = votes
        # d[line[0]] = [int(v) for v in line[3:]]
    return d

def get_democrats(strlist):
    filtered = []
    for line in strlist:
        line = line.strip().split(' ')
        party = line[1]
        if party == 'D':
            filtered.append(line[0])
    return filtered

# Task 2.12.2
def policy_compare(sen_a, sen_b, voting_dict):
    votes_a = voting_dict[sen_a]
    votes_b = voting_dict[sen_b]
    return dot_product(votes_a, votes_b)

def _similar(sen, voting_dict, least=False):
    sens = voting_dict.keys()
    best = ''
    best_score = 0
    for s in sens:
        if s == sen:
            continue
        if best == '':
            best = s
            best_score = policy_compare(sen, s, voting_dict)
        else:
            score = policy_compare(sen, s, voting_dict)
            if (not least and score > best_score) or (least and score < best_score):
                best = s
                best_score = score
    print('_similar: {}, score: {}'.format(best, best_score))
    return best

# Task 2.12.3
def most_similar(sen, voting_dict):
    return _similar(sen, voting_dict, least=False)

# Task 2.12.4
def least_similar(sen, voting_dict):
    return _similar(sen, voting_dict, least=True)

# Task 2.12.7
def find_average_similarity(sen, sen_set, voting_dict):
    total = 0
    for s in sen_set:
        total += policy_compare(sen, s, voting_dict)
    return total*1.0/len(sen_set)

def find_average_record(sen_set, voting_dict):
    sum_vec = None
    for s in sen_set:
        if not sum_vec:
            sum_vec = voting_dict[s]
        else:
            sum_vec = vec_add(sum_vec, voting_dict[s])
    return vec_div(sum_vec, len(sen_set))


if __name__ == "__main__":
    with open('US_Senate_voting_data_109.txt') as f:
        mylist = list(f)
        d = create_voting_dict(mylist)

        # Task 2.12.5
        # most_similar('Chafee', d) # Jeffords
        # least_similar('Santorum', d) # Feingold
        
        # Task 2.12.6
        # print(policy_compare('McConnell', 'Bunning', d)) # 40 pretty high

        democrats = get_democrats(mylist)
        # Task 2.12.7
        # best = 0
        # best_name = ''
        # for sen in d.keys():
        #     a = find_average_similarity(sen, democrats, d)
        #     if a > best:
        #         best = a
        #         best_name = sen
        # print('highest avg similarity Democrat: {}, score: {}'.format(best_name, best)) # highest avg similarity Democrat: Biden, score: 34.8604651163

        # Task 2.12.8
        average_democrat_record = find_average_record(democrats, d)
        print(average_democrat_record)
        best = 0
        best_name = ''
        for sen in d.keys():
            a = dot_product(d[sen], average_democrat_record)
            if a > best:
                best = a
                best_name = sen
                print('new best: {}, score: {}'.format(best_name, best))
        print('highest avg similarity Democrat: {}, score: {}'.format(best_name, best)) # highest avg similarity Democrat: Pryor, score: 31.9302325581
        
        # Task 2.12.9
        # best = 0
        # best_pair = []
        # for outer_sen in d.keys():
        #     for inner_sen in d.keys():
        #         if outer_sen == inner_sen:
        #             continue
        #         score = policy_compare(outer_sen, inner_sen, d)
        #         if score < best:
        #             best = score
        #             best_pair = [outer_sen, inner_sen]
        
        # print('most bitter rivals: {} vs {}, score {}'.format(best_pair[0], best_pair[1], best)) # most bitter rivals: Inhofe vs Feingold, score -3

