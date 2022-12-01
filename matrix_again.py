import numpy as np

class Matrix:

    def __init__(self, matrix):
        self.matrix: list = matrix

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range
                    (len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            return 'Размерности не совпадают'

    def __sub__(self, other):
        if len(self.matrix) == len(other.matrix):
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range
            (len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            return 'Размерности не совпадают'

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(
                [
                    list(map(lambda x: x * other, row))
                    for row in self.matrix
                ]
            )

    def transporting(self):
        return [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]

    @classmethod
    def identity_matrix(cls, m: int, n: int):
        return np.eye(m, n)

    @classmethod
    def null_matrix(cls, m: int, n: int):
        return [[0] * m for i in range(n)]

    @classmethod
    def diagonal_matrix(cls, line: list):
        return np.diag(line)

    def len_matrix(self):
        return len(self.matrix), len([m for m in self.matrix])

    def amount(self):
        return len(self.matrix) * len([m for m in self.matrix])

    def sum_matrix(self):
        return sum(map(sum, self.matrix))

    def no_minus(self):
        return [[number*0 if number < 0 else number for number in line] for line in self.matrix]

    def __eq__(self, other):
        return self.matrix is other.matrix





mm = [
    [-1, 3],
    [0, 1],
    [-2, 2],
]
mm2 = [
    [2, 0],
    [-1, 1],
    [3, -2]
]


matrix1 = Matrix(mm)
matrix2 = Matrix(mm2)
new = matrix1 == matrix2
# new2 = matrix1 * 3
# print(new)
# print(matrix1.transporting())
# print(new2)
# print(Matrix.null_matrix(3, 4))
# print(Matrix.diagonal_matrix([1, 2, 3, 4]))
# print(new)
# print(matrix1.amount())
# print(matrix1.sum_matrix())
print(matrix2.no_minus())
# print(matrix1.len_matrix())

