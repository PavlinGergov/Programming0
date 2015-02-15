n = input("Enter number: ")
n = int(n)

i = 1
s = 0

while i <= n:
    if i%2 == 0:
        s = i + s
        i+=1
    else:
        i+=1
print("Sum is: " + str(s))
