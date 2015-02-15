n = input("Enter number: ")
n = int(n)

i = 1
s = 0

while (True):
    b = n // 10
    if b >= 1:
        a = n%10
        s = a + s
        n = b
    else:
        s = s + n
        print(s)
        break
