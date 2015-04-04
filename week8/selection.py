import copy


def swap(index1, index2, items):
    temp = items[index1]
    items[index1] = items[index2]
    items[index2] = temp


def find_index_of_smallest_number(index, items):
    temp = items[index]
    for i in range(index, len(items)):
        if items[i] < temp:
            temp = items[i]
    return items.index(temp)


def selection_sort(items):
    result = copy.deepcopy(items)
    for i in range(len(result)):
        index = find_index_of_smallest_number(i, result)
        swap(i, index, result)
    return result
