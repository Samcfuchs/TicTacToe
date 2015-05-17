class Interface:
    """Deals with updating board and game arbitration"""
    # Note that player1 will always go first and will
    # always be X. Player2 will be O.
    def __init__(self, player1, player2):
        #super(Interface, self).__init__()
        if player1 = 'player':
            # pull from pvp
        elif player1 = 'roteAI':
            # pull from roteAI
        elif player1 = 'learnAI':
            # pull from learnAI

        if player2 = 'player':
            # pull from pvp
        elif player2 = 'roteAI':
            # pull from roteAI
        elif player2 = 'learnAI':
            # pull from learnAI

        self.result = False
        self.turn = 0
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def is_over:
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

        def turn:
            if self.turn % 0 == 0:
                # call on player1
            else:
                # call on player2
            self.turn += 1

        def return_board:
            # compiles board into a string that is passed to an end.
