board = []
gameagain = True
choice = 0
pure = ''
count = 0
gameagain = True
playerx = 0
playero = 0
win = False
def printboard(board):
    print '''
     %s | %s | %s 
    -----------
     %s | %s | %s 
    -----------
     %s | %s | %s
    ''' % (board[0],board[1],board[2],\
            board[3],board[4],board[5],\
            board[6],board[7],board[8])
def example():
    print '''
     0 | 1 | 2 
    -----------
     3 | 4 | 5 
    -----------
     6 | 7 | 8
    '''
def result(board):
    #top horiz
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or\
       (board[0] == 'O' and board[1] == 'O' and board[2] == 'O'):
        return True
    #mid horiz
    elif (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or\
         (board[3] == 'O' and board[4] == 'O' and board[5] == 'O'):
        return True
    #low horiz
    elif (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or\
         (board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        return True
    
    #left vert
    elif (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or\
         (board[0] == 'O' and board[3] == 'O' and board[6] == 'O'):
        return True
    #mid vert
    elif (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or\
         (board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        return True
    #right vert
    elif (board[2] == 'X' and board[5]  == 'X'and board[8] == 'X') or\
         (board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return True
    
    #left-right diag
    elif (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or\
         (board[0] == 'O' and board[4] == 'O' and board[8] == 'O'):
        return True
    #right-left diag
    elif (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or\
         (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return True
    
    else:
        return False

for i in range(0,9):
    board.append(' ')

while gameagain:
    while not win:
        if count % 2 == 0:
        	player = 'X'
        else:
            player = 'O'
        
        while True:
            pure = input('Player %s:' % (player))
            if pure > 8:
                example()
                continue
            if board[pure] != ' ':
                print 'That has already been picked'
                printboard(board)
            else:
                board[pure] = player
                break
        printboard(board)
        
        count += 1
        win = result(board)
    
	if player == 'X':
        playerx += 1
		print 'PLAYER X WINS'
    else:
        playero += 1
		print 'PLAYER O WINS'
    printboard(board)
    gameagain = input('Play again?')

print 'Player X: %s' % (playerx)
print 'Player O: %s' % (playero)
raw_input()