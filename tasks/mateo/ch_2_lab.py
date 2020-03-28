f = open('voting_record_dump109.txt')
raw_data = list(f)
# data_by_line = []
# for line in raw_data:
#     data_by_line.append(line.split())

# take a list of strings (dataset) and return a dict of last name to list of votes (as ints)
def create_voting_dict(strlist):
    dict_out = {}
    for line in strlist:
        split_line = line.split()
        dict_out[split_line[0]] = [int(item) for item in split_line if split_line.index(item) >= 3]
    return dict_out

def get_list_by_party(strlist, party):
    list_out = []
    for line in strlist:
        split_line = line.split()
        if split_line[1] == party:
            list_out.append(split_line[0])
    return list_out

# return voting match between 2 senators (as dot product)
def policy_compare(sen_a, sen_b, voting_dict):
    dot_prod = 0
    for i in range(len(voting_dict[sen_a])):
        dot_prod += voting_dict[sen_a][i] * voting_dict[sen_b][i]
    return dot_prod

# return name of senator with voting record most similar to given senator
def most_similar(sen, voting_dict):
    max_name = None
    max_count = -1 * policy_compare(sen, sen, voting_dict) # -1 * max agreement = min agreement
    for sen_to_comp in voting_dict:
        if sen_to_comp == sen:
            continue
        results = policy_compare(sen, sen_to_comp, voting_dict)
        if results > max_count:
            max_count = results
            max_name = sen_to_comp

    return max_name

# return name of senator with voting record least similar to given senator
def least_similar(sen, voting_dict):
    min_name = None
    min_count = policy_compare(sen, sen, voting_dict) # max agreement
    for sen_to_comp in voting_dict:
        if sen_to_comp == sen:
            continue
        results = policy_compare(sen, sen_to_comp, voting_dict)
        if results < min_count:
            min_count = results
            min_name = sen_to_comp

    return min_name

# return average similarity of given senator to list of senators
def find_average_similarity(sen, sen_set, voting_dict):
    count = len(sen_set)
    total = 0.0
    for senator in sen_set:
        total += policy_compare(sen, senator, voting_dict)
    return total/count

# find senator who's record is most similar to list of senators provided
def find_max_similar(sen_set, voting_dict):
    running_max = -1 * policy_compare(sen_set[0], sen_set[0], voting_dict) # -1 * max agreement = min agreement
    max_name = None
    for sen in voting_dict:
        result = find_average_similarity(sen, sen_set, voting_dict)
        if result > running_max:
            running_max = result
            max_name = sen
        if sen == 'Wyden':
            print("wyden's similarity: {}".format(result))
    print("max similarity: {}".format(running_max))
    return max_name

def find_average_record(sen_set, voting_dict):
    avg_record = []
    count = len(sen_set)
    for elem in range(len(voting_dict[sen_set[0]])): # total number of votes
        running_total = 0.0
        for sen in sen_set:
            running_total += voting_dict[sen][elem]
        avg_record.append(running_total/count)
    return avg_record

def find_max_similar_to_average(avg_record, voting_dict):
    running_max = -1 * len(voting_dict['Obama'])
    max_name = None
    for sen in voting_dict:
        dot_prod = 0
        for i in range(len(voting_dict[sen])):
            dot_prod += voting_dict[sen][i] * avg_record[i]
        if dot_prod > running_max:
            print("found new best: {}: {}".format(sen, dot_prod))
            running_max = dot_prod
            max_name = sen
        if sen == 'Biden':
            print("biden's similarity: {}".format(dot_prod))
        elif sen == 'Wyden':
            print("wyden's similarity: {}".format(dot_prod))
        elif sen == 'Levin':
            print("levin's similarity: {}".format(dot_prod))
    print("max similarity: {}".format(running_max))
    return max_name

def bitter_rivals(voting_dict):
    running_min = len(voting_dict['Obama'])
    max_name_1 = None
    max_name_2 = None
    for sen in voting_dict:
        for sen_compare in voting_dict:
            if sen != sen_compare:
                result = policy_compare(sen, sen_compare, voting_dict)
                if result < running_min:
                    print("new low result for {} and {}: {}".format(sen, sen_compare, result))
                    max_name_1 = sen
                    max_name_2 = sen_compare
                    running_min = result
    return max_name_1, max_name_2

data_dict = create_voting_dict(raw_data)
dem_list = get_list_by_party(raw_data, "D")
print("dem list: {}".format(dem_list))
average_Democrat_record = find_average_record(dem_list, data_dict)

for i in range(len(data_dict['Biden'])):
    if abs(data_dict['Biden'][i] - data_dict['Wyden'][i]) > 0:
        print("!!!!!!!!!!!!!!!!Biden and Wyden disagree on vote #: {}".format(i))




# print(policy_compare('Kerry', 'Obama', data_dict))
print("most similar to Chafee: {}".format(most_similar('Chafee', data_dict)))
print("least similar to Santorum: {}".format(least_similar('Santorum', data_dict)))
print("average similarity of 'Obama' to Dems: {}".format(find_average_similarity('Obama', dem_list, data_dict)))
#2.12.7
print("senator most similar to average Dem: {}".format(find_max_similar(dem_list, data_dict)))
#2.12.8
print("average record of democrats: {}".format(average_Democrat_record))
print("closest senator to average Dem record: {}".format(find_max_similar_to_average(average_Democrat_record, data_dict)))
print("byden to wdyen similarity: {}".format(policy_compare('Biden', 'Wyden', data_dict)))
#2.12.9
print("the most bitter rivals are: {}".format(bitter_rivals(data_dict)))
