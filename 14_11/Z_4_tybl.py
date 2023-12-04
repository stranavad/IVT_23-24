

def validate_binary(bincislo: str):
    for i1 in range(len(bincislo)):
        if int(bincislo[i1]) != 1 and int(bincislo[i1]) != 0:
            return False

    return True

def parse_binary_into_decimal(bincislo: str) -> int:
    desitkovecislo = 0
    for i2 in range(0, len(bincislo)):
        if int(bincislo[i2]) == 1:
            desitkovecislo += 2 ** (len(bincislo) - 1 - i2)

    return desitkovecislo


def get_highest_mocnina_dvou(cislo: int):
    current = 0

    while 2**current < cislo:
        current += 1

    return current - 1

def parse_decimal_into_binary(dec: int):
    bin = ''
    mocniny = []
    current = get_highest_mocnina_dvou(dec)

    while current > 0:
        mocniny.append(current)
        dec -= 2**current
        current = get_highest_mocnina_dvou(dec)

    if dec == 1:
        mocniny.append(0)

    print(mocniny)

def run():
    bincislo = input('zadej binarni cislo:')

    parse_decimal_into_binary(int(bincislo))
    # print(get_highest_mocnina_dvou(int(bincislo)))

    # if not validate_binary(bincislo):
    #     return
    #
    # print(parse_binary_into_decimal(bincislo))


if __name__ == '__main__':
    run()