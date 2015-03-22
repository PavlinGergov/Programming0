def magic_square(matrix):
    s = []

# Sum of rows:
    for row in matrix:
        s.append(sum(row))
# Sum of columns:
    for i in range(0, len(matrix)):
        s.append(sum([row[i] for row in matrix]))
# Sum of diagonals:
    s.append(sum([matrix[i][i] for i in range(len(matrix))]))

    i = 0
    result = 0
    for j in range(len(matrix) - 1, -1, -1):
        result += matrix[i][j]
        i += 1
    s.append(result)

    return all([s[0] == s[i] for i in range(len(s))])

print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(magic_square([]))
