a = input ("The first number is : ")
a = int(a)
b = input ("The second number is : ")
b = int(b)
oper = input("Select an operator (+ , -, * or / : ")
if oper == "+":
    x = a + b
    print(x)
elif oper == "-":
    x = a - b
    print(x)
elif oper == "*":
    x = a*b
    print(x)
elif oper == "/":
    x = a/b
    print(x)
else:
    print("Unknown operator!")
