#!/usr/bin/env python3

import matutil
from vec import Vec
from GF2 import zero, one
import bitutil

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
    return Vec({0,1,2,3,4,5,6}, {0: zero, 1: zero, 2: zero, 3: zero, 4: zero, 5: zero, 6: zero})

# e = find_error(Vec({0,1,2}, {0: zero, 1: one, 2: zero}))
# print(e)

ct = Vec({0,1,2,3,4,5,6}, {0: one, 1: zero, 2: one, 3: one, 4: zero, 5: one, 6: one})
es = H*ct
e = find_error(es)
c = ct + e
print(c)
p = R * c
print(p)
# 0101

print("Task 4.14.7")
def find_error_matrix(in_mat):
    coldict = matutil.mat2coldict(in_mat)
    errdict = dict()
    for i, v in coldict.items():
        errdict[i] = find_error(v)
    return matutil.coldict2mat(errdict)

test_err_matrix = matutil.listlist2mat(
    [
        [one, zero],
        [one, zero],
        [one, one],
    ]
)
print(find_error_matrix(test_err_matrix))

print("Task 4.14.8")
s = ''.join([chr(i) for i in range(256)])
print(s)

bits = bitutil.str2bits(s)
s_again = bitutil.bits2str(bits)

print(s_again)

print("Task 4.14.9")
s = "what does the fox say?"
P = bitutil.bits2mat(bitutil.str2bits(s))
s_again = bitutil.bits2str(bitutil.mat2bits(P))
print(s_again)

# print("Task 4.14.10")
P = bitutil.bits2mat(bitutil.str2bits("I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."))
# P = bitutil.bits2mat(bitutil.str2bits("testing"))

print("Task 4.14.11")
E = bitutil.noise(P, 0.02)
noisy_P = P + E
print(bitutil.bits2str(bitutil.mat2bits(noisy_P)))

# task 4.14.12
C = G * P
# 4*len(P) bits before and 7*len(P) bits after

print("Task 4.14.13")
Cerr = bitutil.noise(C, 0.02)
Ctilde = C + Cerr

garbled = R * Ctilde
print(bitutil.bits2str(bitutil.mat2bits(garbled)))

# print("Task 4.14.14")
def correct(A):
    err_syn = H*A
    err_mat = find_error_matrix(err_syn)
    return A + err_mat

print("Task 4.14.15")
codewords = correct(Ctilde)
bits = R * codewords
print(bitutil.bits2str(bitutil.mat2bits(bits)))