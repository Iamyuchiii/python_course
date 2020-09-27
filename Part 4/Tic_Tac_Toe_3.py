from tic_tac_to_class import winner

list_tic = [[' ','o',' '],
            [' ','o','x'],
            ['x',' ',' ']]

def play(player, board):
    import random
    if player == "o":
        oponnent = "x"
    elif player == "x":
        oponnent = "o"
    player_win = None
    oponnent_win = None
    random_pos = []
    # loop over every element of list_list
    for i in range(len(board)):
        for j in range(len(board)):
            # if cell is free use player to fill
            if board[i][j] == " ":
                board[i][j] = player
                random_pos.append((i,j))
                # check possible winner in every possible free cells
                if player in winner(board):
                    player_win = (i,j)
                # clear the player that was filled
                board[i][j] = " "
                board[i][j] = oponnent
                # same thing, but check for winning opponent position
                if oponnent in winner(board):
                    oponnent_win = (i, j)
                board[i][j] = " "
    if player_win != None:
        board[player_win[0]][player_win[1]] = player
    elif oponnent_win != None and player_win == None:
        board[oponnent_win[0]][oponnent_win[1]] = player
    else:
        i, j = random.choice(random_pos)
        board[i][j] = player
    return board


print (play("x", list_tic))
