#!/usr/bin/env python

from plotting import plot
import time

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]

# Task 2.3.2
# plot(L, 4)

# Task 2.4.3
def add2(v, w):
    return [v[0]+w[0], v[1]+w[1]]

# plot([add2(v, [1, 2]) for v in L], 5)

# Task 2.5.4
def scalar_vector_mult(alpha, v):
    return [alpha*i for i in v]

# plot([scalar_vector_mult(-0.5, v) for v in L], 4)

# Task 2.6.9
def segment(pt1, pt2):
    return [[(a/99)*pt1[0]+(1-a/99)*pt2[0], (a/99)*pt1[1]+(1-a/99)*pt2[1]] for a in range(100)]

# print(segment([3.5, 3], [0.5, 1]))
# plot(segment([3.5, 3], [0.5, 1]))



time.sleep(1)