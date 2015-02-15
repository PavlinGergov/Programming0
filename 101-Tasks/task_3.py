def ceasar_encrypt(message, n):
    new_string = ""
    
    for i in message:
     
        if (ord(i) >= 65) and (ord(i) <= 90):
            new_i = ord(i) + n
            if new_i > 90:
                new_string += chr(new_i - 26)
            else:
                new_string += chr(new_i)
        elif (ord(i) >= 97) and (ord(i) <= 122):
            new_i = ord(i) + n
            if new_i > 122:
                new_string += chr(new_i - 26)
            else:
                new_string += chr(new_i)
        else:
            new_string += i

    return new_string

message = input("Enter your message: ")
n = input("Enter the key: ")
n = int(n)
print(ceasar_encrypt(message, n))
