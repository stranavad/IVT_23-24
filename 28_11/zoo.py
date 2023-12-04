def get_input():
    with open('animals.txt', 'r') as file:
        raw_lines = file.readlines()
        file.close()
        lines = [x.split('\n')[0] for x in raw_lines]
        animals = lines[0].split(" ")
        sizes = [int(x) for x in lines[1].split(" ")]
        prices = [int(x) for x in lines[2].split(" ")]
        data = [(x[1], prices[x[0]], sizes[x[0]]) for x in enumerate(animals)]
        zoo_size = int(lines[3])
        return data, zoo_size


def do_some_recursion(animals, max_size, n, selected_animals):
    # laast
    if n == 0 or max_size == 0:
        return 0, selected_animals

    # too thick to fit
    if animals[n - 1][2] > max_size:
        return do_some_recursion(animals, max_size, n - 1, selected_animals)

    else:
        # try with current animal
        price_with, new_selected_with = do_some_recursion(
            animals, max_size - animals[n - 1][2], n - 1, selected_animals + [animals[n - 1][0]]
        )

        # try without current animal
        price_without, new_selected_without = do_some_recursion(
            animals, max_size, n - 1, selected_animals
        )

        # choose the besst option
        if price_with + animals[n - 1][1] > price_without:
            return price_with + animals[n - 1][1], new_selected_with
        else:
            return price_without, new_selected_without


def run():
    data, zoo_size = get_input()
    used_animals: list[tuple[str, int, int]] = []
    total_value, total_animals = do_some_recursion(data, zoo_size, len(data), used_animals)
    print(f"Total value: {total_value}")
    print(f"Total animals: {total_animals}")


if __name__ == '__main__':
    run()
