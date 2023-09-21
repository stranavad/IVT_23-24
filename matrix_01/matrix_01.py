from enum import Enum

Matrix = list[list[int]]


def read_instructions(input_file: str) -> tuple[Matrix, Matrix, int]:
    with open(input_file, 'r') as file:
        content = file.readlines()
        file.close()
        joined_matrix = [[int(x) for x in line.split('\n')[0].split(' ')] for line in content[1:]]
        matrix_size = int(content[0])
        return joined_matrix[0:matrix_size], joined_matrix[matrix_size:], matrix_size


def sum(first_matrix: Matrix, second_matrix: Matrix) -> Matrix:
    result: Matrix = []

    for line_index, line in enumerate(first_matrix):
        result.append([])
        for item_index, item in enumerate(line):
            result[line_index].append(item + second_matrix[line_index][item_index])

    return result


def print_matrix(matrix: Matrix):
    for line in matrix:
        print(" ".join([str(x) for x in line]))


def difference(first_matrix: Matrix, second_matrix: Matrix) -> Matrix:
    result: Matrix = []

    for line_index, line in enumerate(first_matrix):
        result.append([])
        for item_index, item in enumerate(line):
            result[line_index].append(item - second_matrix[line_index][item_index])

    return result


class Operation(Enum):
    SUM = 1
    DIFF = 2


def get_operation() -> Operation:
    user_input = input("Do you want to sum them(S) or make a difference(D): ").lower()

    if user_input == 's':
        return Operation.SUM
    elif user_input == 'd':
        return Operation.DIFF

    print("This method does not exist...yet")
    print("Again")
    return get_operation()


def run(input_file: str):
    first_matrix, second_matrix, size = read_instructions(input_file)

    operation = get_operation()

    if operation == Operation.SUM:
        print_matrix(sum(first_matrix, second_matrix))
    elif operation == Operation.DIFF:
        print_matrix(difference(first_matrix, second_matrix))


if __name__ == '__main__':
    path_prepend = "/home/stranavadavid/programming/ivt/ivt01/matrix_01/"
    files = ["01", "02", "03"]
    for file in files:
        run(f"{path_prepend}{file}.in")

