#!/usr/bin/env python3
import matutil
import solver
import vec

from GF2 import one, zero

# Problem 5.14.14
def vec2rep(veclist, v):
    new_bases_mat = matutil.coldict2mat(veclist)
    return solver.solve(new_bases_mat, v)

veclist = []
veclist.append(vec.Vec({0,1,2,3}, {0:1, 2:3}))
veclist.append(vec.Vec({0,1,2,3}, {0:1, 1:2, 2:5, 3:1}))
veclist.append(vec.Vec({0,1,2,3}, {0:1, 1:5, 2:-1, 3:3}))
v = vec.Vec({0,1,2,3}, {0:6, 1:-4, 2:27, 3:-3})

coordinates = vec2rep(veclist, v)
print(coordinates)

gf2_veclist = []
gf2_veclist.append(vec.Vec({0,1,2}, {0:one, 2:one}))
gf2_veclist.append(vec.Vec({0,1,2}, {0:one, 1:one}))
gf2_veclist.append(vec.Vec({0,1,2}, {2:one}))
gf2_v = vec.Vec({0,1,2}, {0:zero, 1:one, 2:one})

gf2_coordinates = vec2rep(gf2_veclist, gf2_v)
print(gf2_coordinates)

# Task 5.12.1
# input: whiteboard coordinates of a point q
# output: whiteboard coordinates of a point p such that the line through the origin and q intersects the whiteboard at p
def move2board(y):
    y['y1'] = y['y1']/y['y3']
    y['y2'] = y['y2']/y['y3']
    y['y3'] = y['y3']/y['y3']
    return y

test_wb_vec_far = vec.Vec({'y1', 'y2', 'y3'}, {'y1': 6, 'y2': 8, 'y3': 2})
print(move2board(test_wb_vec_far))

test_wb_vec_near = vec.Vec({'y1', 'y2', 'y3'}, {'y1': 1, 'y2': 3, 'y3': 0.6})
print(move2board(test_wb_vec_near))

