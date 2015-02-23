def calculate_coins(summ):
    info = {}
    numbs = [100, 50, 20, 10, 5, 2, 1]
    the_sum = summ * 100
    counter = 0
    for numb in numbs:
        while True:
            if the_sum >= numb:
                the_sum = the_sum - numb
                counter += 1
            else:
                info[numb] = counter
                counter = 0
                break
    return info

info = calculate_coins(8.94)
print(info)
