n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers = numbers + [number]
    count += 1
    
i = 0
max_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number

print("Max is: " + str(max_number))
    
