n = input("Enter a number (several digits): ")
n = int(n)

number_list = []

while n // 10 != 0:
    number_list = [n % 10] + number_list
    n = n // 10
else:
    number_list = [n] + number_list

print("The list is: " + str(number_list))

number = 0
for numb in number_list:
    number = number*10 + numb

print("The number is: " + str(number))
