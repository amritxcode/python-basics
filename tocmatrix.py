matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]


result = [[0, 0], [0, 0]]

for i in range(len(matrix_a)):

    for j in range(len(matrix_a[0])):
        
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print(result)
