n = input("Enter a 3 digit number: ")
n = int(n)

a = n % 10
d = n // 10
b = d % 10
c = d // 10

if (a>b) and (a>c):
    high = a
elif (b>a) and (b>c):
    high = b
elif (c>a) and (c>b):
    high = c

if (a<b) and (a<c):
    low = a
elif (b<a) and (b<c):
    low = b
elif (c<a) and (c<b):
    low = c

if (a != low) and (a != high):
    middle = a
elif (b != low) and (b != high):
    middle = b
elif (c != low) and (c != high):
    middle = c


print(str(low) + str(middle) + str(high))
print(str(high) + str(middle) + str(low))
