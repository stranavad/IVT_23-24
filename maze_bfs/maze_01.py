import queue as queue_module

WALL_SYMBOL = 'x'
START_SYMBOL = 's'
FINISH_SYMBOL = 'c'
EMPTY_SYMBOL = '.'


def read_instructions(input_file: str) -> tuple[list[list[str]], int]:
    with open(input_file, 'r') as file:
        content = file.readlines()
        file.close()
        return [line.split('\n')[0].split(' ') for line in content[1:]], int(content[0])


def find_start(board: list[list[str]]) -> tuple[int, int]:
    for line_index, line in enumerate(board):
        for item_index, item in enumerate(line):
            if item.lower() == START_SYMBOL:
                return item_index, line_index


def get_updated_position_on_direction(position: tuple[int, int], direction: str) -> tuple[int, int]:
    if direction == "U":
        return position[0], position[1] - 1
    elif direction == "D":
        return position[0], position[1] + 1
    elif direction == "R":
        return position[0] + 1, position[1]
    elif direction == "L":
        return position[0] - 1, position[1]

    return position


def get_updated_position_on_directions(position: tuple[int, int], directions: str) -> tuple[
    tuple[int, int], list[tuple[int, int]]]:
    visited_positions: list[tuple[int, int]] = []
    updated_position = position

    for direction in directions:
        updated_position = get_updated_position_on_direction(updated_position, direction)
        visited_positions.append(updated_position)

    return updated_position, visited_positions


def check_result(board: list[list[str]], start: tuple[int, int], directions: str) -> bool:
    final_position, _ = get_updated_position_on_directions(start, directions)

    return board[final_position[1]][final_position[0]].lower() == FINISH_SYMBOL


def check_directions_valid(board: list[list[str]], start: tuple[int, int], board_size: int, directions: str) -> bool:
    last_position, visited_positions = get_updated_position_on_directions(start, directions[0:-1])
    target_position = get_updated_position_on_direction(last_position, directions[-1])

    if target_position in visited_positions:
        return False

    if target_position[0] >= board_size or target_position[0] < 0 or target_position[1] >= board_size or \
            target_position[1] < 0:
        return False

    return board[target_position[1]][target_position[0]].lower() != WALL_SYMBOL


def run(input_file: str):
    board, board_size = read_instructions(input_file)
    start = find_start(board)

    queue = queue_module.Queue()
    current = ""
    queue.put(current)

    while not check_result(board, start, current) and not queue.empty():
        current = queue.get()
        for direction in ["U", "D", "R", "L"]:
            current_and_next_move = current + direction
            if check_directions_valid(board, start, board_size, current_and_next_move):
                queue.put(current_and_next_move)

    print("FINISHED")
    solution_valid = check_result(board, start, current)

    if solution_valid:
        print("PATH LENGTH: ", len(current))
        print("PATH: ", current)
        return

    print("This maze cannot be solved")


if __name__ == '__main__':
    path_prepend = "/home/stranavadavid/programming/ivt/ivt01/maze_bfs/"
    mazes = ["1", "2", "3", "4", "5"]

    for maze in mazes:
        run(f"{path_prepend}{maze}.txt")
