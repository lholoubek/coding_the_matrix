#!/usr/bin/env python3

from plotting import plot
import time

# Task 1.4.1
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

# plot(S, 4)

# Task 1.4.10
from image import file2image

data = file2image('img01.png')
# print(data)
pts = {x+y*1j for y in range(len(data)) for x in range(len(data[0])) if data[y][x][0] < 120}
# print(pts)
# pts = {p*0.5*1j for p in pts}
# plot(pts, 190)


# Task 1.4.17
from math import e, pi
w = {e ** ((2*pi*1j)/n) for n in range(1, 20)}
# plot(w)

# Task 1.4.19
pts = {p*e**1j*pi/4 for p in pts}
# plot(pts, 190)

# Task 1.5.1
c = [0b10101, 0b00100, 0b10101, 0b01011, 0b11001, 0b00011, 0b01011, 0b10101, 0b00100, 0b11001, 0b11010]
good_keys = []
for key in range(32):
    bad = False
    for letter in c:
        decoded = key ^ letter
        if int(decoded) > 26:
            bad = True
            break
    if not bad:
        good_keys.append(key)

# print(good_keys)
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
for key in good_keys:
    pt = ''
    for l in c:
        pt += ALPHA[l ^ key]
    print('key={}, plaintext={}'.format(key, pt))

# time.sleep(1)
# print('hi')