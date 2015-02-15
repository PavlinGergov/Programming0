x = input("Select a random number: ")
x = int(x)
first_name = input("Enter your name: ")
second_name = input("Enter your name: ")

from random import randint

first_dice = randint(1,x)
print(first_name + " rolled : " + str(first_dice))
second_dice = randint(1,x)
print(second_name + " rolled : " + str(second_dice))

if int(first_dice) == int(second_dice):
    print("We have a draw!")
elif int(first_dice) > int(second_dice):
    print("The winner is : " + first_name)
else: print("The winner is : " + second_name)
