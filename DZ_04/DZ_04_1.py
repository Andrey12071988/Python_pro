# Напишите функцию для транспонирования матрицы

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 0, 0]]

# Функция
def transpositions (matrix: list) -> list:
    matrix_trans = []
    res = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res.append(matrix[j][i])
        matrix_trans.append(res)
        res = []
    return matrix_trans

# Вывод
for i in mat:
    print(i)
print('')
for i in transpositions(mat):
    print(i)
