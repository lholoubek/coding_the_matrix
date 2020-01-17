#!/usr/bin/env python3

import matutil
from vec import Vec
from GF2 import zero, one

G = matutil.listlist2mat(
    [
        [one, zero, one, one],
        [one, one, zero, one],
        [zero, zero, zero, one],
        [one, one, one, zero],
        [zero, zero, one, zero],
        [zero, one, zero, zero],
        [one, zero, zero, zero],
    ])

print(G*Vec({0,1,2,3}, {0: one, 1: zero, 2: zero, 3: one}))
# 0 0 one one 0 0 one

R = matutil.listlist2mat(
    [
        [zero, zero, zero, zero, zero, zero, one],
        [zero, zero, zero, zero, zero, one, zero],
        [zero, zero, zero, zero, one , zero, zero],
        [zero, zero, one, zero, zero, zero, zero],
    ]
)

print(R*G)
# identity matrix

H = matutil.listlist2mat(
    [
        [zero, zero, zero, one, one, one, one],
        [zero, one, one, zero, zero, one, one],
        [one, zero, one, zero, one, zero, one],
    ]
)

print(H*G)
# zero matrix

possible_e = [
    Vec({0,1,2,3,4,5,6}, {0: one, 1: zero, 2: zero, 3: zero, 4: zero, 5: zero, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: one, 2: zero, 3: zero, 4: zero, 5: zero, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: one, 3: zero, 4: zero, 5: zero, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: one, 4: zero, 5: zero, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: zero, 4: one, 5: zero, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: zero, 4: zero, 5: one, 6: zero}),
    Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: zero, 4: zero, 5: zero, 6: one}),
]
def find_error(err_syndrome):
    for e in possible_e:
        if H*e == err_syndrome:
            return e
    return None

# e = find_error(Vec({0,1,2}, {0: zero, 1: one, 2: zero}))
# print(e)

ct = Vec({0,1,2,3,4,5,6}, {0: one, 1: zero, 2: one, 3: one, 4: zero, 5: one, 6: one})
es = H*ct
e = find_error(es)
c = ct + e
print(c)
p = R * c
print(p)
# 1010

