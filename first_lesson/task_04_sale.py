import utils


def run():
    sale = utils.get_user_input("How big is the sale (in %): ", "number")
    old_price = utils.get_user_input("How much did the album cost before: ", "number")

    if sale >= 100 or sale <= 0:
        print("It's highly unprobable that sale such as this one even exists")
        return

    print(f"New price of the album is {old_price - (old_price * (sale / 100))}")

if __name__ == '__main__':
    run()
