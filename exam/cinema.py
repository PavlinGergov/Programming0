def get_a_starting_point(cinema):
    starting_point = len(cinema[0]) + 1
    for row in cinema:
        if len(row) > starting_point:
            starting_point = len(row) + 1
    return starting_point


def get_index(cinema):
    count = get_a_starting_point(cinema)
    index = None

    for i in range(len(cinema)):
        zero_counter = cinema[i].count(0)
        if zero_counter < count and zero_counter != 0:
            index = i
            count = cinema[i].count(0)

    return index


def order_of_seats(cinema):
    result = []
    while get_index(cinema) is not None:
        index = get_index(cinema)
        for i in range(len(cinema)):
            if i == index:
                for j in range(len(cinema[i])):
                    if cinema[i][j] == 0:
                        result.append((i + 1, j + 1))
                        cinema[i][j] = 1
    return result


def main():
    print(order_of_seats([[1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1]]))

    print(order_of_seats([[1, 1, 1, 0],
                          [1, 0, 1, 0],
                          [0, 0, 0, 0],
                                     ]) == [(1, 4), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)])

    print(order_of_seats([[1, 1, 1],
                          [1, 0, 0],
                          [1, 0, 0],
                          [1, 1, 0] ]) == [(4, 3), (2, 2), (2, 3), (3, 2), (3, 3)])

    print(order_of_seats([[0, 0],
                          [0, 0],
                          [0, 0] ]) == [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)])

if __name__ == '__main__':
    main()
