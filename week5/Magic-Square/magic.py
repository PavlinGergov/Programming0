def magic_square(square):
    sum_all = []
    forward_diagonal = 0
    backward_diagonal = 0
    is_true = True

#Adding every row sum to sum_all
    
    for row in square:
        s = 0
        for element in row:
            s += element
        sum_all.append(s)

#Adding every column sum to sum_all
        
    for i in range(0, len(square)):
        s = 0
        for row in square:
            s += row[i]
        sum_all.append(s)

#Adding the two diagonals to sum_all
        
    for i in range(0, len(square)):
        forward_diagonal += square[i][i]
    sum_all.append(forward_diagonal)
    
    for i in range(len(square) - 1, -1, -1):
        backward_diagonal += square[i][i]
    sum_all.append(backward_diagonal)

#Checking if every element in sum_all is equal

    for i in range(0, len(sum_all)):
        if i + 1 < len(sum_all):
            if sum_all[i] != sum_all[i+1]:
                is_true = False
                break
    return is_true

print(magic_square([ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]))
print(magic_square([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]))
print(magic_square([]))
