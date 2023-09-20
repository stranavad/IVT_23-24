import utils


def run():
    alena_posts = utils.get_user_input("How many posts did alena write: ", "int")
    petr_posts = alena_posts * 2
    pavla_posts = (alena_posts + petr_posts) * 5
    print(f"Alena post count {alena_posts}")
    print(f"Petr post count {petr_posts}")
    print(f"Pavla post count {pavla_posts}")


if __name__ == '__main__':
    run()