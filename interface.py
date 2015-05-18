class Player(object):
    """docstring for Player"""
    def __init__(self, arg):
        #super(Player, self).__init__()
        self.arg = arg


class Game:
    """Deals with updating board and game arbitration"""
    # Note that player1 will always go first and will
    # always be X. Player2 will be O.
    def __init__(self, player1, player2):
        #super(Game, self).__init__()
        if player1 == 'player':
            pass
            # pull from pvp
        elif player1 == 'roteAI':
            pass
            # pull from roteAI
        elif player1 == 'learnAI':
            pass
            # pull from learnAI

        if player2 == 'player':
            pass
            # pull from pvp
        elif player2 == 'roteAI':
            pass
            # pull from roteAI
        elif player2 == 'learnAI':
            pass
            # pull from learnAI

        self.result = False
        self.turn = 0
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def is_over():
        if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or\
           (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
            return True
        #mid horiz
        elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or\
             (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
            return True
        #low horiz
        elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or\
             (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
            return True

        #left vert
        elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or\
             (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
            return True
        #mid vert
        elif (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or\
             (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
            return True
        #right vert
        elif (board[0][2] == 'X' and board[1][2]  == 'X'and board[2][2] == 'X') or\
             (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
            return True

        #left-right diag
        elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or\
             (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
            return True
        #right-left diag
        elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X') or\
             (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
            return True
        else:
            return False

    def turn():
        if self.turn % 0 == 0:
            pass
            # call on player1
        else:
            pass
            # call on player2
        self.turn += 1

    def printboard():
        print '''
         %s | %s | %s
        -----------
         %s | %s | %s
        -----------
         %s | %s | %s
        ''' % (board[0][0][0],board[0][0][1],board[0][0][2],\
               board[0][1][0],board[0][1][1],board[0][1][2],\
               board[0][2][0],board[0][2][1],board[0][2][2])
