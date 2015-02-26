def count_zero_neighours(numbers):
    count = 0
    for i,numb in enumerate(numbers):
        if i + 1 < len(numbers) and numb + numbers[i+1] == 0:
            count += 1
    return count

print(count_zero_neighours([1, 2, -2, 0, 0, 5, -5]))
