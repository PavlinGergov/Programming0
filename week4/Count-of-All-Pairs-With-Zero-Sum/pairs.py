def count_zero_pairs(numbers):
    count = 0
    for i,numb in enumerate(numbers):
        for numb2 in numbers[i:len(numbers)]:
            if numb + numb2 == 0:
                count += 1
    return count

print(count_zero_pairs([0, 2, -2, 5, 10]))
