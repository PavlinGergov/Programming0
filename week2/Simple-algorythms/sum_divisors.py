n = input("Enter a numeber: ")
n = int(n)

i = 1
m = n
s = 0

while i < m:
    is_devisior = False
    if n % i == 0:
        is_devisior = True
        s += i
#    if is_devisior:
#        print(i)
    i+=1
print("The sum is: " + str(s))

