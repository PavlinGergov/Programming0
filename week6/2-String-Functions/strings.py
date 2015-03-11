def str_reverse(word):
    return word[::-1]

def join(delimiter, items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += delimiter
    return result

def startswith(start, word):
    if word[0:len(start)] == start:
        return True
    return False

def endswith(end, word):
    if str_reverse(word)[0:len(end)] == str_reverse(end):
        return True
    return False

def trim(stringg):
    while startswith(" ", stringg):
        stringg = stringg[1:]
    while endswith(" ", stringg):
        stringg = stringg[:len(stringg) - 1]
    return stringg