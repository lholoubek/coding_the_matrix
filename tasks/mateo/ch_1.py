from plotting import plot

# neutral face
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

# rotate by 90 degrees CCW
S2 = {j*point for point in S}

# plot points (and flip apparently) that have intensity of 120 or less
pts = {x + ((len(data)-y)*1j) for x in range(len(data[0])) for y in range(len(data)) if data[y][x][0] <= 120}

# Problem 1.5.1: decoding
C = [21, 4, 21, 11, 25, 3, 11, 21, 4, 25, 26]
D = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '] # list for indexing purposes

# simple offset (WRONG)
P = [[D[(c + mod) % len(D)] for c in C] for mod in range(len(D))
for p in P:
    print(p)

# output: (ALSO WRONG)
['V', 'E', 'V', 'L', 'Z', 'D', 'L', 'V', 'E', 'Z', ' ']
['W', 'F', 'W', 'M', ' ', 'E', 'M', 'W', 'F', ' ', 'A']
['X', 'G', 'X', 'N', 'A', 'F', 'N', 'X', 'G', 'A', 'B']
['Y', 'H', 'Y', 'O', 'B', 'G', 'O', 'Y', 'H', 'B', 'C']
['Z', 'I', 'Z', 'P', 'C', 'H', 'P', 'Z', 'I', 'C', 'D']
[' ', 'J', ' ', 'Q', 'D', 'I', 'Q', ' ', 'J', 'D', 'E']
['A', 'K', 'A', 'R', 'E', 'J', 'R', 'A', 'K', 'E', 'F']
['B', 'L', 'B', 'S', 'F', 'K', 'S', 'B', 'L', 'F', 'G']
['C', 'M', 'C', 'T', 'G', 'L', 'T', 'C', 'M', 'G', 'H']
['D', 'N', 'D', 'U', 'H', 'M', 'U', 'D', 'N', 'H', 'I']
['E', 'O', 'E', 'V', 'I', 'N', 'V', 'E', 'O', 'I', 'J']
['F', 'P', 'F', 'W', 'J', 'O', 'W', 'F', 'P', 'J', 'K']
['G', 'Q', 'G', 'X', 'K', 'P', 'X', 'G', 'Q', 'K', 'L']
['H', 'R', 'H', 'Y', 'L', 'Q', 'Y', 'H', 'R', 'L', 'M']
['I', 'S', 'I', 'Z', 'M', 'R', 'Z', 'I', 'S', 'M', 'N']
['J', 'T', 'J', ' ', 'N', 'S', ' ', 'J', 'T', 'N', 'O']
['K', 'U', 'K', 'A', 'O', 'T', 'A', 'K', 'U', 'O', 'P']
['L', 'V', 'L', 'B', 'P', 'U', 'B', 'L', 'V', 'P', 'Q']
['M', 'W', 'M', 'C', 'Q', 'V', 'C', 'M', 'W', 'Q', 'R']
['N', 'X', 'N', 'D', 'R', 'W', 'D', 'N', 'X', 'R', 'S']
['O', 'Y', 'O', 'E', 'S', 'X', 'E', 'O', 'Y', 'S', 'T']
['P', 'Z', 'P', 'F', 'T', 'Y', 'F', 'P', 'Z', 'T', 'U']
['Q', ' ', 'Q', 'G', 'U', 'Z', 'G', 'Q', ' ', 'U', 'V']
['R', 'A', 'R', 'H', 'V', ' ', 'H', 'R', 'A', 'V', 'W']
['S', 'B', 'S', 'I', 'W', 'A', 'I', 'S', 'B', 'W', 'X']
['T', 'C', 'T', 'J', 'X', 'B', 'J', 'T', 'C', 'X', 'Y']
['U', 'D', 'U', 'K', 'Y', 'C', 'K', 'U', 'D', 'Y', 'Z']

# using RF(2)
P = [[D[(c^p) % len(D)] for c in C] for p in range(31)]
for p in P:
    print(p)

['V', 'E', 'V', 'L', 'Z', 'D', 'L', 'V', 'E', 'Z', ' ']
['U', 'F', 'U', 'K', 'Y', 'C', 'K', 'U', 'F', 'Y', 'A']
['X', 'G', 'X', 'J', 'A', 'B', 'J', 'X', 'G', 'A', 'Y']
['W', 'H', 'W', 'I', ' ', 'A', 'I', 'W', 'H', ' ', 'Z']
['R', 'A', 'R', 'P', 'C', 'H', 'P', 'R', 'A', 'C', 'D']
['Q', 'B', 'Q', 'O', 'B', 'G', 'O', 'Q', 'B', 'B', 'E']
['T', 'C', 'T', 'N', 'E', 'F', 'N', 'T', 'C', 'E', 'B']
['S', 'D', 'S', 'M', 'D', 'E', 'M', 'S', 'D', 'D', 'C']
['C', 'M', 'C', 'D', 'R', 'L', 'D', 'C', 'M', 'R', 'S']
['B', 'N', 'B', 'C', 'Q', 'K', 'C', 'B', 'N', 'Q', 'T']
['E', 'O', 'E', 'B', 'T', 'J', 'B', 'E', 'O', 'T', 'Q']
['D', 'P', 'D', 'A', 'S', 'I', 'A', 'D', 'P', 'S', 'R']
['Z', 'I', 'Z', 'H', 'V', 'P', 'H', 'Z', 'I', 'V', 'W']
['Y', 'J', 'Y', 'G', 'U', 'O', 'G', 'Y', 'J', 'U', 'X']
['A', 'K', 'A', 'F', 'X', 'N', 'F', 'A', 'K', 'X', 'U']
[' ', 'L', ' ', 'E', 'W', 'M', 'E', ' ', 'L', 'W', 'V']
['F', 'U', 'F', 'A', 'J', 'T', 'A', 'F', 'U', 'J', 'K']
['E', 'V', 'E', ' ', 'I', 'S', ' ', 'E', 'V', 'I', 'L'] # <--
['H', 'W', 'H', 'Z', 'L', 'R', 'Z', 'H', 'W', 'L', 'I']
['G', 'X', 'G', 'Y', 'K', 'Q', 'Y', 'G', 'X', 'K', 'J']
['B', 'Q', 'B', 'E', 'N', 'X', 'E', 'B', 'Q', 'N', 'O']
['A', 'R', 'A', 'D', 'M', 'W', 'D', 'A', 'R', 'M', 'P']
['D', 'S', 'D', 'C', 'P', 'V', 'C', 'D', 'S', 'P', 'M']
['C', 'T', 'C', 'B', 'O', 'U', 'B', 'C', 'T', 'O', 'N']
['N', 'B', 'N', 'T', 'B', 'A', 'T', 'N', 'B', 'B', 'C']
['M', 'C', 'M', 'S', 'A', ' ', 'S', 'M', 'C', 'A', 'D']
['P', 'D', 'P', 'R', 'D', 'Z', 'R', 'P', 'D', 'D', 'A']
['O', 'E', 'O', 'Q', 'C', 'Y', 'Q', 'O', 'E', 'C', 'B']
['J', 'Y', 'J', 'X', 'F', 'E', 'X', 'J', 'Y', 'F', 'G']
['I', 'Z', 'I', 'W', 'E', 'D', 'W', 'I', 'Z', 'E', 'H']
['L', ' ', 'L', 'V', 'H', 'C', 'V', 'L', ' ', 'H', 'E']

P = [[D[c^p] if (c^p<len(D)) else '-' for c in C] for p in range(31)] # instead of using mod