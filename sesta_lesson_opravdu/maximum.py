def run():
    # Nechce se mi osetrovat vstupy
    numbers = [float(x) for x in input('Vstup: ').split()]
    max = (float('-inf'), 0)  # value, index
    for index, number in enumerate(numbers):
        if number > max[0]:
            max = (number, index)

    print(max)

if __name__ == '__main__':
    run()