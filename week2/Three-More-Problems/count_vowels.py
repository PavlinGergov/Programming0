message = input("Enter a message: ")
counter = 0
glasni_bukvi = "aeiouyAEIOUY"

for asd in message:
    if asd in glasni_bukvi:
        counter += 1

print(message + " - " + str(counter))
