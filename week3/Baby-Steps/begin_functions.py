def square(x):
    return x ** 2

def fact(n):
    i = 1
    fac = 1
    if n == 0:
        fac = 1
    else:
        while i <= n:
            fac *= i
            i += 1

    return fac

def count_elements(items):
    counter_of_elements = 0
    for element in items:
        counter_of_elements += 1

    return counter_of_elements

def member(x, xs):
    is_seen = False
    for element in xs:
        if x == element:
            is_seen = True

    return is_seen

def grades_that_pass(students, grades, limit):
    index = 0
    passed_students = []
    for student in students:
        if grades[index] >= limit:
            passed_students += [student]

        index += 1
            

    return passed_students

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]
print(grades_that_pass(students, grades, 4.0))
        
    
        
        
    
