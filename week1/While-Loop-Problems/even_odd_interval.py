a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)

if a < b:
    start = a
    end = b
elif a > b:
    start = b
    end = a

i = start

while i <= end:
    if (i%2 == 0):
        print(str(i) + " - " + "even")
    else:
        print(str(i) + " - " + "odd")
    i+=1
