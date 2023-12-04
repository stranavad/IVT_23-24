def parse_binary_into_decimal(binary: str) -> int:
    total = 0

    for bit_index in range(len(binary)):
        if int(binary[bit_index]) == 1:
            total += 2 ** (len(binary) - bit_index - 1)

    return total


def run():
    user_input = input('Enter number (in binary): ')
    print(parse_binary_into_decimal(user_input))


if __name__ == '__main__':
    run()
