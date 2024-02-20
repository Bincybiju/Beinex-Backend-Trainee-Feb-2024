""" Write a Python program to perform matrix multiplication using lists of lists.
"""

def matrix(rows, cols):
    
    matrix = []
    print(f"Enter elements for {rows} x {cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element at position ({i+1}, {j+1}): ")))
        matrix.append(row)
    return matrix

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be  multiplied.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result

rows1 = int(input("Enter the number of rows for matrix1: "))
cols1 = int(input("Enter the number of columns for matrix1: "))
matrix1 = matrix(rows1, cols1)

rows2 = int(input("Enter the number of rows for matrix2: "))
cols2 = int(input("Enter the number of columns for matrix2: "))
matrix2 = matrix(rows2, cols2)

result = matrix_multiplication(matrix1, matrix2)

if result:
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
