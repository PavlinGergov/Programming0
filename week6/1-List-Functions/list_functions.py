def head(n):
    return n[0]

def last(n):
    return n[len(n) - 1]

def tail(n):
    n.remove(n[0])
    return n

def equal_lists(l1,l2):
    if len(l1) == len(l2):
        if l1 == l2:
            return True
        else:
            return False

def count_item(item, n):
    count = 0
    for element in n:
        if item == element:
            count += 1
    return count

def take(n, listt):
    return listt[0:n]

def drop(n, listt):
    return listt[n:len(listt)]

def reverse(listt):
    return listt[::-1]