def resetGame():
    board=[['-','-','-'],['-','-','-'],['-','-','-']]
    return board

def printBoard(board):
    for x in range(0, len(board)):
        print(str(board[x]) + "\n")

def checkWinner(board):
    for x in range(0, len(board)):#horizontal
        if board[x][0]== board[x][1] and board[x][1] == board[x][2] and not (board[x][1]== '-'):
            print( str(board[x][1]) + " is the winner!")
            return board[x][1]
    for x in range(0, len(board)):#vertical
        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and not (board[1][x]== '-'):
            print( str(board[1][x]) + " is the winner!")
            return board[1][x]
    #Diagonals
    if board[0][0] == board[1][1] and board [1][1] == board[2][2] and not board[1][1] == '-':
        print( str(board[1][1]) + " is the winner!")
        return board[1][1]
    if board[0][2] == board[1][1] and board [1][1] == board[2][0] and not board[1][1] == '-':
        print( str(board[1][1]) + " is the winner!")
        return board[1][1]
    if '-' in board[0] or  '-' in board[1] or '-' in board[2]:
        print( "there are no winners yet!")
        return 'NONE'
    else:
        print( "This game is a tie!")
        return 'DONE'

def playerHit(board, player):
    print("Player, " + player + ", it is your turn!")
    while (True):
        x= int(input('Please select your x coordinate: '))
        y= int(input('Please select your y coordinate: '))
        if x > 3 or y >3 or y<1 or x <1:
            print("You cannot play here, this is out of bounds")
        elif not board[x-1][y-1] == '-':
            print("You cannot override another player's turn")
        else:
            break
    board[x-1][y-1] = player
    return board


if __name__ == '__main__':
    response='1'
    while response == '1':
        board= resetGame()
        winner=checkWinner(board)
        printBoard(board)
        while winner == 'NONE':
            playerHit(board, 'X')
            printBoard(board)
            winner=checkWinner(board)
            if not winner== 'NONE':
                break
            print('\n')
            playerHit(board, 'O')
            printBoard(board)
            winner=checkWinner(board)
        response = str(input("Press 1 to play again! "))
        print('\n\n\n\n\n')
