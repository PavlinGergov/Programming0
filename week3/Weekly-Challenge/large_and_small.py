from prime_digits import to_digits

def to_int(k):
    the_number = 0
    for numb in k:
        the_number = the_number*10 + numb

    return the_number

def large(m):
    largest = sorted(to_digits(m), reverse=True)    
    return largest

def small(m):
    lowest = sorted(to_digits(m))
    return lowest

m = input("Enter a number: ")
m = int(m)

if 0 in large(m):
    print("There is 0 in the number you've entered." + 
          "I have no right to do this task!")
else:
    print("Largest is: " + str(to_int(large(m))))
    print("Smallest is: " + str(to_int(small(m))))
