a = input ("The first number is : ")
a = int(a)
b = input ("The second number is : ")
b = int(b)
oper = input("Select an operator (+ , -, * or / : ")
if oper == "+":
    x = a + b
    print("The result is: " + str(x))
elif oper == "-":
    x = a - b
    print("The result is: " + str(x))
elif oper == "*":
    x = a*b
    print("The result is: " + str(x))
elif oper == "/":
    x = a/b
    print("The result is: " + str(x))
else:
    print("Unknown operator!")
