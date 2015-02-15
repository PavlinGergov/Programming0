word = input("Enter a word: ")

n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    second_word = input("Enter the other words: ")

    numbers = numbers + [second_word]

    count += 1
    
i = 0
p = 0

for asd in numbers:
    if word in asd:
        p+=1
        
print(word + " is found " + str(p) + " times.")

    
