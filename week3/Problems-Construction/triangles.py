import math

def max_number(x):
    if len(x) == 0:
        max_numb = 0
        return max_numb

    max_numb = x[0]
    for i in x:
        if i > max_numb:
            max_numb = i
    return max_numb

def is_triangle(a, b, c):
    sides = [a, b, c]
    s = 0
    for side in sides:
        if side != max_number(sides):
            s += side
    if max_number(sides) < s:
        return True
    else:
        return False

def area(a, b, c):
    S = 0
    if is_triangle(a, b, c):
        p = (a + b + c) / 2
        S = (p*(p-a)*(p-b)*(p-c))
        S = math.sqrt(S)
    return S

def is_pythagorean(a, b, c):
    numbs = [a, b, c]
    s = 0
    if is_triangle(a, b, c):
        for num in numbs:
            if num != max_number(numbs):
                s += num ** 2
    if s == max_number(numbs) ** 2:
        
        return True
    else:
        return False

def max_area(triangles):
    maxim = 0
    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]

        if is_triangle(a, b, c):
            new_area = area(a, b, c)
        if new_area > maxim:
            maxim = new_area
    return maxim

print(max_area([ [7, 8, 9], [3, 4, 5] ]))
