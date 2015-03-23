def magic_square(matrix):
    s = []

# Sum of rows:
    for row in matrix:
        s.append(sum(row))
# Sum of columns:
    for i in range(0, len(matrix)):
        s.append(sum([row[i] for row in matrix]))
# Sum of main diagonal:
    s.append(sum([matrix[i][i] for i in range(len(matrix))]))
# Sum of second diagonal:
    i = 0
    result = 0
    for j in range(len(matrix) - 1, -1, -1):
        result += matrix[i][j]
        i += 1
    s.append(result)

    return all([s[0] == s[i] for i in range(len(s))])

print(magic_square([ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]))
print(magic_square([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]))
print(magic_square([
	[8, 58, 59, 5, 4, 62, 63, 1],
	[49, 15, 14, 52, 53, 11, 10, 56],
	[41, 23, 22, 44, 45, 19, 18, 48],
	[32, 34, 35, 29, 28, 38, 39, 25],
	[40, 26, 27, 37, 36, 30, 31, 33],
	[17, 47, 46, 20, 21, 43, 42, 24],
	[9, 55, 54, 12, 13, 51, 50, 16],
	[64, 2, 3, 61, 60, 6, 7, 57]]))
