from random import randint

first_player = input("Selet name 1: ")
second_player = input("Select name 2: ")

first_score = 1001
second_score = 1001


while (True):
    if (first_score != 0) and (second_score != 0):
        if (first_score > 0) and (second_score > 0):
            first_score = first_score - (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            second_score = second_score - (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            print(first_score)
            print(second_score)
        elif (first_score < 0) and (second_score > 0):
            first_score = first_score + (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            second_score = second_score - (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            print(first_score)
            print(second_score)
        elif (first_score > 0) and (second_score < 0):
            first_score = first_score - (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            second_score = second_score + (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            print(first_score)
            print(second_score)
        elif (first_score < 0) and (second_score < 0):
            first_score = first_score + (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            second_score = second_score + (randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6))
            print(first_score)
            print(second_score)
    else:
        if first_score == 0:
            print("The winner is: " + first_player)
            break
        elif second_score == 0:
            print("The winner is: " + second_player)
            break
        
