n = input("Enter number: ")
n = int(n)

if n == 1:
    print("1 is not a prime number.")

i = 2

while i < n:
    if (n % i) == 0:
        print(str(n) + " is not a prime number.")
        break
    else:
        i+=1
    if i == n:
        print(str(n) + " is prime number.")
    
