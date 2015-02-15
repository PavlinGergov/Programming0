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

if is_prime(n) and is_prime(n-2) and is_prime(n+2):
    print("Twin primes with " + str(n))
    print(str(n-2) + ", " + str(n))
    print(str(n) + ", " + str(n+2))
