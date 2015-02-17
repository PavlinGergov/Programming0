def is_prime(n):
    start = 2
    is_prime = True
    
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
        
    return is_prime

n = input("Enter a number: ")
n = int(n)

if is_prime(n):
    print(str(n) + " is prime.")
else:
    print(str(n) + " is not prime.")
    
if is_prime(n-2):
    print(str(n-2) + " is twin prime.")
if is_prime(n+2):
    print(str(n+2) + " is twin prime.")
