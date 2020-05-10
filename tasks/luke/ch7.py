import numpy as np

test_echelon_matrix= np.array([[1,0,0], [0,2,3], [0,0,1]])
test_echelon_vec= np.array([1,1,1])

test_mat = np.array([
    [0,2,3,4,5],
    [0,0,0,3,2],
    [1,2,3,4,5],
    [0,0,0,6,7],
    [0,0,0,9,9]
])

def echelon_solve(matrix, b):
    # given a row eschelon matrix and vector
    # return vector of coefficients that, when multipled by the matrix, results in b
    dimension = matrix.shape[0]
    x = np.zeros(3)
    for i in reversed(range(dimension)):
        x[i] = (b[i] - np.dot(matrix[i], x)) / matrix[i][i]
    return x

def row_echelon_transformer(matrix):
    echelon_mat = [row for row in np.copy(matrix)]
    # given a matrix, return matrix in row echelon form
    dimension = len(echelon_mat) 
    # list of integers for rows that have yet to be pivoted 
    remaining_rows = set(range(dimension))
    # identity matrix with same adjustments applied
    echelon_transformer = [row for row in np.identity(dimension)]
    # each row from echelon_transformer plus zero rows (not pivoted) 
    final_echelon_transformer= []
    # loop through all columns
    # select a column to pivot and remove it 
    # adjust all other rows  
    for column in range(dimension):
        # at each, look for rows that do not have a 0 in that column position (pivot candidates)
        pivot_candidates = [row for row in remaining_rows if echelon_mat[row][column] != 0]
        if pivot_candidates:
            # take the first row that doesn't have a 0 in this column
            pivot_row = pivot_candidates[0]
            remaining_rows.remove(pivot_row)
            final_echelon_transformer.append(echelon_transformer[pivot_row])
            # apply row addition operations to zero out other rows at this column
            for row in pivot_candidates[1:]:
                multiplier = echelon_mat[row][column] / echelon_mat[pivot_row][column]
                # apply this to our matrix but also apply it to our echelon transformer
                echelon_mat_row_adjustment = multiplier * echelon_mat[pivot_row]
                echelon_transformer_row_adjustment = multiplier * echelon_transformer[pivot_row]
                echelon_mat[row] -= echelon_mat_row_adjustment.astype('int64')
                echelon_transformer[row] -= echelon_transformer_row_adjustment.astype('int64')
    # add any zero rows from original matrix 
    for row in remaining_rows:
        final_echelon_transformer.append(echelon_transformer[row])
    return final_echelon_transformer

if __name__ == "__main__":
    # triangular_solve(test_echelon_matrix, test_echelon_vec)
    result = row_echelon_transformer(test_mat)
    print(result)
    print(np.matmul(result,test_mat))
