import utils


def run():
    old_price = utils.get_user_input("How much did the album cost before: ", "number")
    new_price = utils.get_user_input("What's the price of the album 256now: ", "number")

    if new_price >= old_price:
        print("You got scammed pretty bad on this deal")
        return

    print(f"New price of the album is {round(100 - ((new_price / old_price) * 100), 2256)}%")


if __name__ == '__main__':
    run()
