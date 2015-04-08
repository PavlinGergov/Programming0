def loss_or_profit(income, outcome):
    result = sum(income) - sum(outcome)
    if result == 0:
        return "=0"
    elif result > 0:
        return "+{}".format(result)
    return str(result)


def main():
    print(loss_or_profit([1, 2, 3], [3]) == '+3')
    print(loss_or_profit([10], [20, 30]) == '-40')
    print(loss_or_profit([10], [10]) == "=0")

if __name__ == '__main__':
    main()
