a = input("Enter the lower bound: ")
a = int(a)
b = input("Enter the upper bound: ")
b = int(b)
x = input("Enter x: ")
x = int(x)

if x == a:
    print("The number is equal to the lower bound of the interval.")
elif x == b:
    print("The number is equal to the upper bound of the interal.")
elif (x > a) and (x < b):
    print("The number is in the interval.")
elif a > x:
    print("The number is outside the interval, x < a.")
elif x > b:
    print("The number is outside the interval, x > b.")

