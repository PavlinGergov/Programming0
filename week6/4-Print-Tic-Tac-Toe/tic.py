def join(delimiter, items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += delimiter
    return result

def board_to_string(board):
    result = "| "
    for i in range(len(board)):
        board[i] = " | ".join(board[i])
    result += join(" |\n| ", board)
    result += " |"
    return result

print(board_to_string([ ["X", "O", "#"],
                        ["X", "X", "X"],
                        ["#", "#", "#"] ]))