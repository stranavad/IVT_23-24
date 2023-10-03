import queue as queue_module
from first_lesson.utils import get_user_input


def run(capacity_a: int, capacity_b: int, target_a: int, target_b: int):
    visited: list[tuple[int, int]] = []
    queue = queue_module.Queue()
    queue.put(((0, 0), 0))

    while not queue.empty():
        (a, b), steps = queue.get()
        visited.append((a, b))

        if a == target_a and b == target_b:
            print(steps)
            print("LZE")
            return

        options = []

        if a > 0:
            options.append((0, b))

        if b > 0:
            options.append((a, 0))

        if a < capacity_a:
            options.append((capacity_a, b))

        if b < capacity_b:
            options.append((a, capacity_b))

        if b < capacity_b and a > 0:
            vol = min(capacity_b - b, a)
            options.append((a - vol, b + vol))

        if a < capacity_a and b > 0:
            vol = min(capacity_a - a, b)
            options.append((a + vol, b - vol))

        for option in options:
            if not option in visited:
                queue.put((option, steps + 1))

    print("nelze")


if __name__ == '__main__':
    capacity_a = get_user_input("Capacity A", "int")
    capacity_b = get_user_input("Capacity B", "int")
    target_a = get_user_input("Target A", "int")
    target_b = get_user_input("Target B", "int")

    if not (target_a > capacity_a or target_b > capacity_b or capacity_a < 0 or capacity_b < 0 or target_a < 0 or target_b < 0):
        run(capacity_a, capacity_b, target_a, target_b)
