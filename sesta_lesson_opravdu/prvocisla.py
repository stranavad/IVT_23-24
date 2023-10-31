def run():
    rozkladance = []
    n = int(input("Zadejte přirozené číslo: "))
    i = 2

    while i <= n:
        if n % i == 0:
            rozkladance.append(i)
            n = n / i
        else:
            i += 1

    print("Rozkladance: ", " * ".join([str(x) for x in rozkladance]))


if __name__ == '__main__':
    run()