n = input("Enter n: ")
n = int(n)
m = input("Enter m: ")
m = int(m)

if n > m:
    start = m
    end = n
elif n < m:
    start = n
    end = m

while start <= end:
    i = start
    s = 0
    
    while i != 0:
        s += i % 10
        i = i // 10
    else:
        s += i
        print("The sum of digits of " + str(start) + " = " + str(s))

    start += 1
