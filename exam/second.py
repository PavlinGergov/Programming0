def second_largest(numbers):
    if len(numbers) < 2:
        return False
    max_number1 = max(numbers)
    while max(numbers) == max_number1:
        numbers.remove(max_number1)
        if len(numbers) == 0:
            return False
    return max(numbers)


def main():
    print(second_largest([]) == False)
    print(second_largest([2, 1]) == 1)
    print(second_largest([5, 5]) == False)
    print(second_largest([100, 100, 90]) == 90)

if __name__ == '__main__':
    main()
