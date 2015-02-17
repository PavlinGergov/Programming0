def devisors(n):
    i = 1
    numbers = []
    while i < n:
        if n % i == 0:
            numbers += [i]
            
        i+=1

    return numbers

