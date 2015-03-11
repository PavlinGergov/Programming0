def join(delimiter, items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += delimiter
    return result

def board_to_string(board):
    result = []
    res = []
    for item in board:
        current = ""
        for element in item:
            current += element
        result.append(join(" | ", current))
    for item in result:
        print(item)
    return result




print(board_to_string([ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]))