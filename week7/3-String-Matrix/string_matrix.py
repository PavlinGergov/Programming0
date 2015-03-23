def row_string(string):
    result = []
    for ch in string:
        result += [ch]
    return result


def string_matrix(number_strings, strings) :
    matrix = []
    for string in strings:
        matrix.append(row_string(string))
    for row in matrix:
        while len(row)>number_strings:
            del row[-1]
        if len(row)<number_strings:
            while number_strings>len(row):
                row.append("X")
    return matrix


board = string_matrix(6,["pyth","gogo","aloha","java","haskell","rubyOnRails"])


def board_to_string(board) :
    for row in board:
        print("|", " | ".join(row),"|")


board_to_string(board)