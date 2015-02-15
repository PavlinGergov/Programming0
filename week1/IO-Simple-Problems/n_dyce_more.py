x = input("Select a number: ")
from random import randint
y = int(x)
a = randint(1,y)
print("First roll: " + str(a))
b = randint(1,y)
print("Second roll: " + str(b))
c = randint(1,y)
print("Third roll: " + str(c))
sum = a + b + c
print("The total sum is = " + str(sum))
