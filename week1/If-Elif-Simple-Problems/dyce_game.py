x = input("Select a random number: ")
y = int(x)
first_name = input("Your name is: ")
second_name = input("Your name is: ")

from random import randint

first_dyce = randint(1,y)
print("The first roll is : " + str(first_dyce))
second_dyce = randint(1,y)
print("The second roll is : " + str(second_dyce))

if int(first_dyce) == int(second_dyce): print("We have a draw!")
else:
    if int(first_dyce) > int(second_dyce):print("The winner is : " + first_name)
    else: print("The winner is : " + second_name)
