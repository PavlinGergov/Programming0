n = input("Enter a numeber: ")
n = int(n)

start = 6

while True:
    s = 0
    i = 1

    while i < start:
        if start % i == 0:
            s += i

        i += 1

    if s == start:
        print(s)
        n -= 1
    
    if n == 0:
        break

    start += 1
