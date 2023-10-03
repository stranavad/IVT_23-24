def summaries(number, current=None, start=1):
    if current is None:
        current = []

    if number == 0:
        return [current]

    if number < start:
        return []

    results = []

    for i in range(start, number + 1):
        results.extend(summaries(number - i, current + [i], i))

    return results


def print_summaries(data: list[list[int]]):
    for summary in data:
        print("+".join(map(str, summary)))


if __name__ == '__main__':
    # Nechce se mi validovat input
    n = int(input("Zadej N: "))
    res = summaries(n)
    print_summaries(res)
