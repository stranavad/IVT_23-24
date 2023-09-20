import utils


def run():
    money = utils.get_user_input('How much money do you have: ', 'number')
    payment = utils.get_user_input("How much does it cost: ", 'number')

    if (money - payment) < 0:
        print("It looks like you can't afford this")
        return

    print(f"Balance after payment {money - payment}")


if __name__ == '__main__':
    run()