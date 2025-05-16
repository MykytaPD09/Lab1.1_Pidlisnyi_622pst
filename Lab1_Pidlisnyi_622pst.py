import numpy as np

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Матриця не є оберненою"

def matrix_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def gauss_method(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return "Система не має розв'язку або має нескінченно багато розв'язків"

A = np.array([[-2, 5, -1], [-1, 4, -2], [1, 3, -2]])
b = np.array([4, 5, 6])

print('Обернена матриця A:')
print(inverse_matrix(A))

print('\nРанг матриці A:')
print(matrix_rank(A))

print("\nРозв'язок СЛАР методом Гауса:")
print(gauss_method(A, b))