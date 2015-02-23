fname = input("First name: ")
sname = input("Second name: ")
lname = input("Last name: ")
bday = int(input("Bday year: "))

age = 2015 - bday

info = {
        'first_name' : fname,
        'second_name': sname,
        'third_name': lname,
        'birth_year': bday,
        'current_age': age,
        }
print(info)
