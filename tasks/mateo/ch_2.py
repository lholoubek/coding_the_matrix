import time

from ch_1_the_field.plotting import plot

# Task 2.3.2
L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75,1], [3,1], [3.25,1]]
#plot(L, 4)

def add2(v,w):
    return [v[0]+w[0], v[1]+w[1]]

#plot([add2(v, [1,2]) for v in L], 4)

# Task 2.6.9
def segment(pt1, pt2):
    return [[pt1[0]*(1-i/99) + pt2[0]*i/99, pt1[1]*(1-i/99) + pt2[1]*i/99] for i in range(100)]

pt1 = [3.5, 3]
pt2 = [0.5, 1]
# plot(segment(pt1, pt2), 4)

# Computational Problem 2.8.7
# input: a vector s and a list L of vectors over GF(2)
# output: a subset of the vectors in L whose sum is s, or a report that there is no such subset



print(results)


time.sleep(1)
