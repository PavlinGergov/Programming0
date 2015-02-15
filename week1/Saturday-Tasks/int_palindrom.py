n = input("Enter number: ")
n = int(n)

k = n
a = n % 10
x = str(a)
n = n // 10

while n // 10 != 0:
    b = n % 10
    x = x + str(b)
    n = n // 10
else:
    x = x + str(n)

h = int(x)

if k == h:
    print("The number is palindrom.")
else:
    print("The number is not a polindrom.")
        
