import bitutil
import matutil
import vec
from GF2 import one, zero

g_by_rows = []
g_by_rows.append([one, 0, one, one])
g_by_rows.append([one, one, 0, one])
g_by_rows.append([0, 0, 0, one])
g_by_rows.append([one, one, one, 0])
g_by_rows.append([0, 0, one, 0])
g_by_rows.append([0, one, 0, 0])
g_by_rows.append([one, 0, 0, 0])

print("printing g_by_rows")
print(g_by_rows)
G = matutil.listlist2mat(g_by_rows)
print("printing G")
print(G)

h_by_rows = []
h_by_rows.append([0, 0, 0, one, one, one, one])
h_by_rows.append([0, one, one, 0, 0, one, one])
h_by_rows.append([one, 0, one, 0, one, 0, one])
H = matutil.listlist2mat(h_by_rows)
print(h_by_rows)
print(H)

print(H*G)

r_by_rows = []
r_by_rows.append([0, 0, 0, 0, 0, 0, one])
r_by_rows.append([0, 0, 0, 0, 0, one, 0])
r_by_rows.append([0, 0, 0, 0, one, 0, 0])
r_by_rows.append([0, 0, one, 0, 0, 0, 0])
R = matutil.listlist2mat(r_by_rows)

# Task 4.14.5
def find_error(v):
    assert v.D == H.D[0]
    ret = vec.Vec(H.D[1], {})
    if v[0] == one:
        if v[1] == one:
            if v[2] == one:
                ret[6] = one
            else:
                ret[5] = one
        elif v[2] == one:
            ret[4] = one
        else:
            ret[3] = one
    elif v[1] == one:
        if v[2] == one:
            ret[2] = one
        else:
            ret[1] = one
    elif v[2] == one:
        ret[0] = one
    return ret

# Task 4.14.6
bad_code_word = vec.Vec({0, 1, 2, 3, 4, 5, 6}, {0: one, 1: 0, 2: one, 3: one, 4: 0, 5: one, 6: one})
print(H.D)
print(bad_code_word.D)
e_syndrome = H * bad_code_word
print(e_syndrome)
e = find_error(e_syndrome)
print("error: ", e)
corrected_code_word = bad_code_word + e
print("corrected_core_word: ", corrected_code_word)
print("plaintext: ", R*corrected_code_word)

# Task 4.14.7
def find_error_matrix(S):
    # go through each column in S (an error syndrome) and c
    # error_matrix_by_columns = {}
    # for col in S.D[1]:
    #     error_matrix_by_columns[col] = find_error(matutil.mat2coldict(S)[col])
    # return matutil.coldict2mat(error_matrix_by_columns)
    return matutil.coldict2mat({col: find_error(matutil.mat2coldict(S)[col]) for col in S.D[1]})

test_by_rows = []
test_by_rows.append([one, 0])
test_by_rows.append([one, 0])
test_by_rows.append([one, one])

print(find_error_matrix(matutil.listlist2mat(test_by_rows)))

# Task 4.14.10
P = bitutil.bits2mat(bitutil.str2bits("I'm trying to free your mind, Neo. But I can only show you the door. You're the one that has to walk through it."))
E = bitutil.noise(P, 0.02)
print(bitutil.bits2str(bitutil.mat2bits(P + E)))

# Task 4.14.12
C = G*P

# Task 4.14.13
C_error = bitutil.noise(C, 0.02)
CTILDE = C + C_error
print(bitutil.bits2str(bitutil.mat2bits(R * CTILDE)))

# Task 4.14.14
def correct(A):
    # H * A # gives us a matrix of error syndromes for each codeword
    # find_error_matrix(H * A) # gives us a matrix of error vectors
    return A + find_error_matrix(H * A)

print(bitutil.bits2str(bitutil.mat2bits(R * correct(CTILDE))))
