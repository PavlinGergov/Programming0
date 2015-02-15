n = input("Enter number: ")
n = int(n)

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
print(h)

