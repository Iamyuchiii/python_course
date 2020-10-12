list_tic = [[' ','o',' '],[' ','o','x'],['x','x',' ']]

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

theBoard["7"], theBoard["8"], theBoard["9"] = list_tic[0][0], list_tic[0][1], list_tic[0][2]
theBoard["4"], theBoard["5"], theBoard["6"] = list_tic[1][0], list_tic[1][1], list_tic[1][2]
theBoard["1"], theBoard["2"], theBoard["3"] = list_tic[2][0], list_tic[2][1], list_tic[2][2]


def printBoard(board):
    print(" " + board['7'] + " " + '|' + " " + board['8'] + " " + '|' + " " + board['9'])
    print('---+---+---')
    print(" " + board['4'] + " " + '|' + " " + board['5'] + " " + '|' + " " + board['6'])
    print('---+---+---')
    print(" " + board['1'] + " " + '|' + " " + board['2'] + " " + '|' + " " + board['3'])

printBoard(theBoard)

# def tic_tac_toe(state):
#     c = 0
#     for n in state:
#         print(' {0} | {1} | {2} '.format(n[0], n[1], n[2]))
#         c += 1
#         if c < len(state):
#             print('{:11}'.format('---+---+---'))
#
# if __name__ == '__main__':
#     state = [[' ','o',' '],[' ','o','x'],['x','x',' ']]
#     tic_tac_toe(state)