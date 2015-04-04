def setify(a):
    return list(set(a))


def diff(a, b):
    diff_a = [numb for numb in a if numb not in b]
    diff_b = [numb for numb in b if numb not in a]
    return diff_a + diff_b


def union(a, b):
    result = []
    for numb in a:
        if numb not in result:
            result.append(numb)
    for numb in b:
        if numb not in result:
            result.append(numb)
    return result


def intersection(a, b):
    return [numb for numb in a if numb in b]


def cartesian_product(a, b):
    return [(x, y) for x in a for y in b]


def main():
    print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
    print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
    print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
    print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
    print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


if __name__ == '__main__':
    main()
