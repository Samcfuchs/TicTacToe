class Game:
    """Deals with updating board and game arbitration"""
    # Note that player1 will always go first and will
    # always be X. Player2 will be O and go second.
    def __init__(self):
        self.result = False
        self.turn = 0
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    
    def playerpick(self):
        print 'PLAYERPICK EXECUTED'
        player1 = raw_input('Player 1: ').lower()
        player2 = raw_input('Player 2: ').lower()
        # Add ends to this list as they are created
    
        if player1 == 'human':
            from human import Human
            self.player1 = Human(1, self)
        elif player1 == 'roteai':
            raise RuntimeError
        elif player1 == 'learnai':
            #player1 = learnAI()
            pass
        else:
            from human import Human
            self.player1 = Human(1, self)
    
        if player2 == 'human':
            from human import Human
            self.player2 = Human(2, self)
        elif player2 == 'roteai':
            raise RuntimeError
        elif player2 == 'learnai':
            #player2 = learnAI()
            pass
        else:
            from human import Human
            player2 = Human(2, self)
        
        print
             
    def is_over(self):
        if (self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X') or\
           (self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O'):
            return True
        #mid horiz
        elif (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X') or\
             (self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O'):
            return True
        #low horiz
        elif (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X') or\
             (self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O'):
            return True

        #left vert
        elif (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X') or\
             (self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O'):
            return True
        #mid vert
        elif (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X') or\
             (self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O'):
            return True
        #right vert
        elif (self.board[0][2] == 'X' and self.board[1][2]  == 'X'and self.board[2][2] == 'X') or\
             (self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O'):
            return True

        #left-right diag
        elif (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or\
             (self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O'):
            return True
        #right-left diag
        elif (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X') or\
             (self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'):
            return True
        else:
            return False

    def print_board(self):
        print '''
         %s | %s | %s
        -----------
         %s | %s | %s
        -----------
         %s | %s | %s
        ''' % (self.board[0][0],self.board[0][1],self.board[0][2],\
               self.board[1][0],self.board[1][1],self.board[1][2],\
               self.board[2][0],self.board[2][1],self.board[2][2])

    def play(self):
        # TODO
        turn = 0
#       print
#       print self
#       print
        while self.is_over() == False:
            if turn % 2 == 0:
                one = self.player1
                self.player1.turn()
            elif turn % 2 == 1:
                two = self.player2
                self.player2.turn()
            turn += 1
