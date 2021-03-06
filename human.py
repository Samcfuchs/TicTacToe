# Human Player program end
from interface import *

class Human:
    """interface for a human player"""
    def __init__(self, player, gameinstance):
        #super(Human, self).__init__()
        from interface import Game
        self.gameinstance = gameinstance
        self.keymap = [7,8,9,4,5,6,1,2,3] # matches numpad on keyboard
        self.choice = None
        self.player = player
        self.print_player()
        self.result = []
        try:
            if input('Set a keymap? (0/1) '):
                self.set_keymap()
            else:
                self.print_keymap()
        except SyntaxError:
            self.print_keymap()
    def set_keymap():
        # TODO
        pass

    def print_player(self):
        print "PLAYER " + str(self.player)
        print "========"

    def print_keymap(self):
        print 'This is your current keymap:'
        # print diagram of keymap
        print '''
         %s | %s | %s
        -----------
         %s | %s | %s
        -----------
         %s | %s | %s
        ''' % (self.keymap[0],self.keymap[1],self.keymap[2],\
               self.keymap[3],self.keymap[4],self.keymap[5],\
               self.keymap[6],self.keymap[7],self.keymap[8])

    def turn(self):
        # TODO
        self.print_player()
        print 'Board:'
        self.gameinstance.print_board()
#        Game.print_board(self.gameinstance)
#        print self.gameinstance.board
        print
        print 'Keymap:'
        self.print_keymap()
        print
        # Now we need to convert the user's input, given based on the keymap, a
        # value in the board. This is apparently difficult. In the end, turn
        # should pass a tuple of the values it wants back to the Game()

        # Temporarily assuming keymap is default - tests input validity
        while True:
            # Checks if input is a number
            try:
                self.choice = int(raw_input('Pick a square: '))
                if self.choice not in keymap:
                    raise ValueError
                # Convert choice to tuple
                c = self.choice
                if c == 7:
                    self.result = (0,0)
                elif c == 8:
                    self.result = (0,1)
                elif c == 9:
                    self.result = (0,2)
                elif c == 4:
                    self.result = (1,0)
                elif c == 5:
                    self.result = (1,1)
                elif c == 6:
                    self.result = (1,2) 
                elif c == 1:
                    self.result = (2,0)
               elif c == 2:
                    self.result = (2,1)
                elif c == 3:
                    self.result = (2,2)
                else:
                    raise ValueError
            except ValueError:
                print 'Please enter a valid number'
                continue
            finally:
		return self.list
