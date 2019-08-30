from plotting import plot

# neutral face
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}

# rotate by 90 degrees CCW
S2 = {j*point for point in S}

# plot points (and flip apparently) that have intensity of 120 or less
pts = {x + ((len(data)-y)*1j) for x in range(len(data[0])) for y in range(len(data)) if data[y][x][0] <= 120}

# decode
C = [21, 4, 21, 11, 25, 3, 11, 21, 4, 25, 26]
D = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
P = [[D[(c + mod) % len(D)] for c in C] for mod in range(len(D))
for p in P:
    print(p)

# output:
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
