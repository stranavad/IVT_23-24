from first_lesson.utils import get_user_input


def run():
    n = get_user_input('Enter n: ', 'int')

    sequence = []

    for i in range(0, n):
        if i == 0:
            sequence.append(0)
            continue

        if i == 1:
            sequence.append(1)
            continue

        sequence.append(sequence[i - 1] + sequence[i - 2])

    # jednoradkovy iterator, ktery prevede array intu na array stringu
    # A nasledne je spoji do jednoho stringu pomocni newline characteru \n
    print("\n".join([str(x) for x in sequence]))


if __name__ == '__main__':
    run()
