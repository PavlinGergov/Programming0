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
s = 0

for number in numbers:
    s += number
    
avg = s / len(numbers)

print("Avg is: " + str(avg))
    
