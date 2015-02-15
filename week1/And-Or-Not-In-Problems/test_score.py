x = input("Enter the result from the test: ")
x = int(x)

if (x >= 0) and (x <= 50):
    print("Slab 2.")
elif (x > 50) and (x <= 60):
    print("Sreden 3.")
elif (x > 60) and (x <= 70):
    print("Dobyr 4.")
elif (x > 70) and (x <= 80):
    print("Mnogo Dobyr 5.")
elif (x > 80) and (x <= 99):
    print("Otlichen 6.")
elif x == 100:
    print("Mnogo Otlichen 7.")
