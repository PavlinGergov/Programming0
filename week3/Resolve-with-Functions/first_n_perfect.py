from devisors import devisors
from sum_devisors import sum_ints
from is_perfect import is_perfect

def first_n_perfect(y):
    perfect_numbers = []
    start = 6
    while True:
        if is_perfect(start):
            perfect_numbers += [start]
            y -= 1

        if y == 0:
            break

        start += 1

    return perfect_numbers

print(first_n_perfect(3))
        
            
