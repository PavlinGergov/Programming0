def how_many_blocks_can_see(numbers):    
    counter = 1
    i = 1
    

    if len(numbers) == 0:
        return 0

    max_blok = numbers[0]
    
    while i < len(numbers):
        if numbers[i] > max_blok:
            counter += 1
            max_blok = numbers[i]
        i += 1

    return counter

n = input("Enter the count of blocks: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter the height of the block: ")
    number = int(number)
    numbers = numbers + [number]
    count += 1

if how_many_blocks_can_see(numbers) == 0:
    print("Иванчо ще види празно люлинско поле!")
elif how_many_blocks_can_see(numbers) == 1:
    print("Иванчо ще види " + str(how_many_blocks_can_see(numbers)) + " блок.")
else:
    print("Иванчо ще види " + str(how_many_blocks_can_see(numbers)) + " блока.")
  
