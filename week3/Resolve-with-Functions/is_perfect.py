from devisors import devisors
from sum_devisors import sum_ints

def is_perfect(n):
    is_it_perfect = False
    
    if sum_ints(devisors(n)) == n:
        is_it_perfect = True
        
    return is_it_perfect

