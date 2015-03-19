def taken_name(surname_husband, surname_wife):
    if surname_husband in surname_wife: 
        return True 
    return False

surname_husband = input('Enter husband surname: ') 
surname_wife = input('Enter wife surname: ') 
print()

def main():
    if taken_name(surname_husband , surname_wife): 
        print ('The wife has taken her husband\'s surname.') 
    else: 
        print ('The wife has not taken her husband\'s surname.')

if __name__ == '__main__':
    main()