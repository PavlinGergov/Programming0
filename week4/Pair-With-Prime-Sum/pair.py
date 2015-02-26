def is_prime(n):
    start = 2
    is_prime = True
    
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
        
    return is_prime

def prime_pair(numbers):
    result = False
    for i,numb in enumerate(numbers):
        for numb2 in numbers[i:len(numbers)]:
            if is_prime(numb + numb2):
                result = True
    return result

print(prime_pair([1, 2, 3, 4, 5]))
