n = input("Enter number: ")
n = int(n)
m = input("Enter number: ")
m = int(m)

a = n%10
b = m%10

if a > b:
    print(n)
elif a < b:
    print(m)
elif a == b:
    if n > m:
        print(n)
    elif n < m:
        print(m)
