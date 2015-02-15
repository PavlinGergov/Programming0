n = input("Enter number: ")
n = int(n)

i = 1
s = 0

while (True):
    b = n // 10
    if b > 0:
        a = n % 10
        s += a
        n = b
    else:
        s += n
        print(s)
        break
