import math
import utils


def run():
    radius = utils.get_user_input('Input for radius:', 'number')
    print(f"Obsah kruhu: {math.pi * pow(radius, 2)}")
    print(f"Obvod kruhu: {2 * math.pi * radius}")


if __name__ == '__main__':
    run()
