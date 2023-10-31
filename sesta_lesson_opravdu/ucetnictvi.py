def run():
    people = ["Matous", "Matousek", "Lukase", "Adamek"]
    debt = [69, 420, 134, 96]


    for person_index, person in enumerate(people):
        print(f"{person} mi dluzi {debt[person_index]}")


if __name__ == '__main__':
    run()