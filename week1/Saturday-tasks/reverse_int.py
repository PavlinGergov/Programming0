n = input("Enter number: ")
n = int(n)

a = n%10
x = str(a)
#print(x)

while (True):
    y = n // 10
    if y != 0:
        b = y % 10
        x = x + str(b)
        n = y
    else:
#        print(x)
        break

h = int(x)
print(h)

#print(h)
        
