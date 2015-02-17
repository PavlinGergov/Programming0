def is_prime(n):
    start = 2
    is_prime = True
    
    while start < n:
        if n % start == 0:
            is_prime = False
            break
        
        start += 1
        
    return is_prime

def to_digits(n):
    digits_list = []
    while n // 10 != 0:
        digits_list += [n % 10]
        n = n // 10
    else:
        digits_list += [n]

    return digits_list

