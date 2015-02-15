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
while i < len(numbers):
    if max_number < numbers[i]:
        max_number = numbers[i]
        i+=1
    else:
        i+=1
print("Max is: " + str(max_number))
    
