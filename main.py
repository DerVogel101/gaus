from pprint import pprint
from copy import deepcopy


matrix = [[2, 3, 1, 1],
          [4, -1, 3, 11],
          [3, 1, -1, 0]]

for a, i0 in enumerate(matrix):
    for b, i1 in enumerate(i0):
        matrix[a][b] = float(i1)

matrix_len = len(matrix)

for top_index, matrix_line in enumerate(matrix):
    for edit_index, edit_line in enumerate(matrix):
        if not edit_index == top_index:
            temp = deepcopy(matrix[edit_index][top_index] / matrix[top_index][top_index])
            for lpos, lpos_val in enumerate(edit_line):
                matrix[edit_index][lpos] -= temp * matrix[top_index][lpos]

for index in range(matrix_len):
    temp_div = deepcopy(matrix[index][index])
    for col_index in range(matrix_len + 1):
        matrix[index][col_index] /= temp_div

if matrix_len <= 3:
    ords = [120, 121, 122]
else:
    ...


# temp = deepcopy(matrix[1][0] / matrix[0][0])
# matrix[1][0] -= temp * matrix[0][0]
# matrix[1][1] -= temp * matrix[0][1]
# matrix[1][2] -= temp * matrix[0][2]
# matrix[1][3] -= temp * matrix[0][3]
#
# temp = deepcopy(matrix[2][0] / matrix[0][0])
# matrix[2][0] -= temp * matrix[0][0]
# matrix[2][1] -= temp * matrix[0][1]
# matrix[2][2] -= temp * matrix[0][2]
# matrix[2][3] -= temp * matrix[0][3]
#
#
# temp = deepcopy(matrix[0][1] / matrix[1][1])
# matrix[0][0] -= temp * matrix[1][0]
# matrix[0][1] -= temp * matrix[1][1]
# matrix[0][2] -= temp * matrix[1][2]
# matrix[0][3] -= temp * matrix[1][3]
#
# temp = deepcopy(matrix[2][1] / matrix[1][1])
# matrix[2][0] -= temp * matrix[1][0]
# matrix[2][1] -= temp * matrix[1][1]
# matrix[2][2] -= temp * matrix[1][2]
# matrix[2][3] -= temp * matrix[1][3]
#
#
# temp = deepcopy((matrix[0][2] / matrix[2][2]))
# matrix[0][0] -= temp * matrix[2][0]
# matrix[0][1] -= temp * matrix[2][1]
# matrix[0][2] -= temp * matrix[2][2]
# matrix[0][3] -= temp * matrix[2][3]
#
# temp = deepcopy(matrix[1][2] / matrix[2][2])
# matrix[1][0] -= temp * matrix[2][0]
# matrix[1][1] -= temp * matrix[2][1]
# matrix[1][2] -= temp * matrix[2][2]
# matrix[1][3] -= temp * matrix[2][3]
#
# pprint(matrix)
#
# temp = deepcopy(matrix[0][0])
# matrix[0][0] = matrix[0][0] / temp
# matrix[0][3] = matrix[0][3] / temp
#
# temp = deepcopy(matrix[1][1])
# matrix[1][1] = matrix[1][1] / temp
# matrix[1][3] = matrix[1][3] / temp
#
# temp = deepcopy(matrix[2][2])
# matrix[2][2] = matrix[2][2] / temp
# matrix[2][3] = matrix[2][3] / temp

pprint(matrix)

# x, y, z = matrix[0][3], matrix[1][3], matrix[2][3]
#
# print(f"x= {x}\ny= {y}\nz= {z}")
