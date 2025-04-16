def read_matrix(file_path):
    with open(file_path, "r") as file:
        content = file.read().split("\n\n")
    matrices = []
    for matrix_str in content:
        rows = matrix_str.strip().split("\n")
        matrix = []
        for row in rows:
            elements = [int(x) for x in row.split(",")]
            matrix.append(elements)
        matrices.append(matrix)
    return matrices


def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result


def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result


def print_matrix(matrix):
    for row in matrix:
        print(",".join(map(str, row)))


def main(file_path, operation):
    # file_path = input("Enter file path containing matrices: ")
    matrices = read_matrix(file_path)
    if len(matrices) != 2:
        print("Error: File must contain exactly two matrices separated by blank line.")
        return

    matrix1, matrix2 = matrices
    print("Matrix 1:")
    print_matrix(matrix1)
    print("\nMatrix 2:")
    print_matrix(matrix2)

    # operation = input("\nSelect operation (+, -, *): ").strip()
    if operation == "+":
        result = matrix_addition(matrix1, matrix2)
        if result is None:
            print("Error: Matrix dimensions don't match for addition.")
        else:
            print("\nAddition result:")
            print_matrix(result)
    elif operation == "-":
        result = matrix_subtraction(matrix1, matrix2)
        if result is None:
            print("Error: Matrix dimensions don't match for subtraction.")
        else:
            print("\nSubtraction result:")
            print_matrix(result)
    elif operation == "*":
        result = matrix_multiplication(matrix1, matrix2)
        if result is None:
            print("Error: Matrix dimensions don't match for multiplication.")
        else:
            print("\nMultiplication result:")
            print_matrix(result)
    else:
        print("Error: Invalid operation.")


if __name__ == "__main__":
    main("./Group project2/Q8_test_case1.txt", "*")
    main("./Group project2/Q8_test_case2.txt", "-")
