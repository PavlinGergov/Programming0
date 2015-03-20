n = int(input("Enter an odd number: "))


def sandclock(n):
    initial_numb = n
    result = []
    counter = 1
    while n >= 1:
        dots = "."*counter
        stars = "*"*n
        result.append(dots + stars + dots)
        n -= 2
        counter += 1
    else:
        n = 1
        counter -= 1
        while n <= initial_numb - 2:
            n += 2
            counter -= 1
            dots = "."*counter
            stars = "*"*n
            result.append(dots + stars + dots)
    return result


def main():
    if n % 2 == 0:
        print("\n" + str(n) + " is not an odd number, please enter another number.")
    else:
        for element in sandclock(n):
            print(element)


if __name__ == '__main__':
    main()