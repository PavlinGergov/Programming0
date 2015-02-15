n = input("Enter a numeber: ")
n = int(n)

i = 1
m = n

while i < m:
    is_devisior = False
    if n % i == 0:
        is_devisior = True
    if is_devisior:
        print(i)
    i+=1


