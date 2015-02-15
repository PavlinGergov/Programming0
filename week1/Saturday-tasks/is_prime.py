n = input("Enter number: ")
n = int(n)

i = 2

if n > 1:
    while i < n:
        if (n % i) == 0:
            print(str(n) + " is not  prime number")
            break
        else:
            i+=1
        if i == n:
            print(str(n) + " is prime number")
    
