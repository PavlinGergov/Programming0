n = input("Enter a number: ")
n = int(n)

numbers = []
prime_numbers = [2,3,5,7]
is_there_prime = False

while n // 10 != 0:
    numbers += [n%10]
    n = n// 10
else:
    numbers += [n]

for number in numbers:
    if number in prime_numbers:
        is_there_prime = True
if is_there_prime:
    print("DA")
else:
    print("NE")
