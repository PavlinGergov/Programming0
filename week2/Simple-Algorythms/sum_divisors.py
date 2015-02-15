n = input("Enter a number: ")
n = int(n)

i = 1
numbers = []

while i < n:
    if n % i == 0:
        numbers += [i]
    i+=1

s = 0
for numb in numbers:
    s += numb

print(s)




