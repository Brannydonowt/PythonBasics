# reference for matrices

import numpy as np

# a matrix is basically a list of lists
# for example 
A = [[1, 2, 3], [4, 5, 6]]

# this creates a 3 x 2 matrix (3 columns, 2 rows)

# lets explore a matrix a bit more
B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print (B[0][1]) # = 2
print (B[1][0]) # = 5
print (B[2][0] + B[0][3]) # = 8 + 4 = 12

print(np.matrix(B))

# can we make a 3D matrix? o.o
C = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]
print(C[0][0][0]) # = 0
print(C[0][1][2]) # = 5
# this is cool but god knows how I'll ever use this practically...