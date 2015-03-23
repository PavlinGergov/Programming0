import re
def is_string_palindrome(string):
    string = re.sub('[.,;:!?]', ' ', string)
    string = ("".join(string.split())).lower()
    reversed_string = string[::-1].lower()
    if string == reversed_string:
        return True
    return False
print(is_string_palindrome("Az obi4am ma4 I boza"))
print(is_string_palindrome("A Toyota!"))
print(is_string_palindrome("bozaaa"))
print(is_string_palindrome(" kapak! "))