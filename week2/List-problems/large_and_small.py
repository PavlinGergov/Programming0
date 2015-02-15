n = input("Enter a huge number: ")
n = int(n)

numbers = []

while n // 10 != 0:
    if n // 10 != 0:
        x = n % 10
        numbers += [x]
        n = n // 10
else:
    numbers += [n]

low_numbers = sorted(numbers)
max_numbers = sorted(numbers, reverse=True)

i = 0
base = 10
max_number = 0
low_number = 0

while i < len(low_numbers):
    max_number += (base**i)*low_numbers[i]
    i+=1

print("The largest number is: " + str(max_number))
i = 0

while i < len(max_numbers):
    low_number += (base**i)*max_numbers[i]
    i+=1

print("The lowest number is: " + str(low_number))
