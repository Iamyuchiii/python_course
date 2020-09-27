def winner(board):
    result = []
    x_win = False
    o_win = False
    # length of the board (horizontal)
    for i in range(len(board)):
        # only for non-diagonal wins
        count_x_hor = 0
        count_o_hor = 0
        count_x_ver = 0
        count_o_ver = 0
        # width of the board (vertical)
        for j in range(len(board[i])):
            if board[i][j] == "x":
                count_x_hor += 1
            if board[i][j] == "o":
                count_o_hor += 1
            if board[j][i] == "x":
                count_x_ver += 1
            if board[j][i] == "o":
                count_o_ver += 1
        # check for wins, if win then the condition becomes true
        if count_x_hor == len(board) or count_x_ver == len(board[i]):
            x_win = True

        if count_o_hor == len(board) or count_o_ver == len(board[i]):
            o_win = True

        # only for diagonal wins
    count_x_diag1 = 0
    count_o_diag1 = 0
    count_x_diag2 = 0
    count_o_diag2 = 0
    for i in range(len(board)):
        if board[i][i] == "x":
            count_x_diag1 += 1
        if board[i][len(board) - 1 - i] == "x":
            count_x_diag2 += 1
        if board[i][i] == "o":
            count_o_diag1 += 1
        if board[i][len(board) - 1 - i] == "o":
            count_o_diag2 += 1


    if count_x_diag1 == len(board) or count_x_diag2 == len(board):
        x_win = True
    elif count_o_diag1 == len(board) or count_o_diag2 == len(board):
        o_win = True

    if x_win and o_win:
        result=["It's a draw"]
    elif x_win:
        result=["The winner is player", "x"]
    elif o_win:
        result=["The winner is player", "o"]
    else:
        result=["nobody won"]

    return result

board_1 = [['x', 'o', 'x'],
           ['o', 'o', 'x'],
           ['x', 'x', 'o']]

board_2 = [[' ', 'o', ' '],
           [' ', 'o', 'x'],
           ['x', 'o', ' ']]
