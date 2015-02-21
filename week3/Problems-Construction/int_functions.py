def reverse_int(n):
    a = n % 10
    x = str(a)
    n = n // 10
    while n // 10 != 0:
        b = n % 10
        x = x + str(b)
        n = n // 10
    else:
        x = x + str(n)
    h = int(x)
    return h

def sum_digits(n):
    i = 1
    s = 0
    while (True):
        b = n // 10
        if b > 0:
            a = n % 10
            s += a
            n = b
        else:
            s += n
            break
    return s

def product_digits(n):
    i = 1
    p = 1
    while (True):
        b = n // 10
        if b > 0:
            a = n % 10
            p *= a
            n = b
        else:
            p *= n
            break
    return p

