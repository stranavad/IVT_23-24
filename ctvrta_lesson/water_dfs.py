def run(capacity_a: int, capacity_b: int, target_a: int, target_b: int):
    path = []  # Could also best, but values should not appear twice anyway
    solution_path = []
    min_steps = float('inf')

    def dfs(current: tuple[int, int], steps: int):
        nonlocal path, min_steps, solution_path

        if current == (target_a, target_b):
            if steps < min_steps:
                min_steps = steps
                solution_path = path[:]
                return
            return

        if steps > min_steps:
            return

        a, b = current

        # Empty A
        if a > 0:
            new = (0, b)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

        # Empty B
        if b > 0:
            new = (a, 0)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

        # Fill A
        if a < capacity_a:
            new = (capacity_a, b)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

        # Fill B
        if b < capacity_b:
            new = (a, capacity_b)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

        # From A -> B
        if b < capacity_b and a > 0:
            vol = min(capacity_b - b, a)
            new = (a - vol, b + vol)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

        # From B -> A
        if a < capacity_a and b > 0:
            vol = min(capacity_a - a, b)
            new = (a + vol, b - vol)

            if new not in path:
                path.append(new)
                dfs(new, steps + 1)
                path.pop()

    dfs((0, 0), 0)

    if min_steps == float('inf'):
        print('Nelze')
        return

    print("Lze")
    print(solution_path)
    print(min_steps)


if __name__ == '__main__':
    run(3, 2, 2, 1)
