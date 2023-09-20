import utils


def run():
    width = utils.get_user_input("What's the width: ", "number")
    length = utils.get_user_input("What's the length: ", "number")
    circle_count = utils.get_user_input("How many circles will you run:", "number")

    total_length = 2 * (width + length) * circle_count
    print(f"You'll run total of {total_length}m")


if __name__ == '__main__':
    run()
