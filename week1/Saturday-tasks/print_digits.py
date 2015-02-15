n = input("Enter number: ")
n = int(n)

i = 1


while (True):
    b = n // 10
    if b >= 1:
        a = n%10
        print(a)
        n = b
    else:
        print(n)
        break
    
