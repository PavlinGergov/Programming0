def count_zero_neighours(numbers):
    count = 0
    for i,numb in enumerate(numbers):
        if i + 1 < len(numbers) and numb + numbers[i+1] == 0:
            count += 1
    return count

print(count_zero_neighours([2, 1, -2, 3, -3, 0, 4, -5]))
