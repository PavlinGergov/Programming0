from random import randint
def generate_random_list(n, start, end):
    i = 0
    numbs = []
    while i < n:
        numbs.append(randint(start, end))
        i += 1
    return numbs

n = int(input("Enter n: "))
start = int(input("Enter the start: "))
end = int(input("Enter the end: "))
print(generate_random_list(n, start, end))
