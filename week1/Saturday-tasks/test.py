i = input()
i = int(i)
p = 0
while (i // 10) > 9:
    p = (i % 10) + p
    i = i // 10
else:
    p = (i // 10) + (i % 10) + p
    print(str(p))
