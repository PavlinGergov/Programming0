a = input("N = ")
b = input("M = ")
a = int(a)
b = int(b)

if a > b:
    start = b
    end = a
elif a < b:
    start = a
    end = b

i = start
s = 0
p = 0

while i <= end:
    k = i
    h = i
    while (i // 10) != 0:
        if (i // 10) > 9:
            while (h // 10) > 9:
                p = (h % 10) + p
                h = h // 10
            else:
                p = (h // 10) + (h % 10) + p
                print("Sum of digits of " + str(k) + " = " + str(p))
                print("I am the 1st print")
                p = 0
                i+=1
                break
        else:
            s = (i // 10) + (i % 10)
            print("Sum of digits of " + str(i) + " = " + str(s))
            print("I am the second print")
            i+=1
            break
    else:
        s = i
        print("Sum of digits of " + str(i) + " = " + str(s))
        print("I am the third print")
        i+=1
        
        
