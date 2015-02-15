# books.py

book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
counter = 1
book2_name = "Learn You a Haskell"
book2_price = 0
counter += 1
book3_name = "The Healthy Programmer"
book3_price = 50
counter += 1
book4_name = "Code Complete"
book4_price = 60
counter += 1
book5_name = "The Pragmatic Programmer"
book5_price = 20
counter += 1
book6_name = "Pro Git"
book6_price = 0
counter += 1
book7_name = "Introduction to Algorithms"
book7_price = 80
counter += 1
book8_name = "Concrete Mathematics"
book8_price = 100
counter += 1

print(book1_name + "has price: " + str(book1_price))
print(book2_name + "has price: " + str(book2_price))
print(book3_name + "has price: " + str(book3_price))
print(book4_name + "has price: " + str(book4_price))
print(book5_name + "has price: " + str(book5_price))
print(book6_name + "has price: " + str(book6_price))
print(book7_name + "has price: " + str(book7_price))
print(book8_name + "has price: " + str(book8_price))

sum = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price
cena = 0.75*(book7_price + book8_price)

print("Total sum = " + str(sum))
print("Total counter is = " + str(counter))
print("Cenata sled nameleneto e = " + str(cena))
print("Books we can buy are 5. They are: ")
print(book2_name)
print(book6_name)
print(book1_name)
print(book5_name)
print(book3_name)

print("I hate this task :)")
