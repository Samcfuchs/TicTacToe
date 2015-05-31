# Human Player program end
from interface import *

class Human:
    """interface for a human player"""
    def __init__(self, player):
        #super(Human, self).__init__()
        from interface import Game
        self.keymap = [7,8,9,4,5,6,1,2,3] # matches numpad on keyboard
        self.choice = None
        self.player = player
        self.print_player()
        if input('Set a keymap? (0/1) '):
            self.set_keymap()
        else:
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
        print_player()
        print 'Board:'
        Game.print_board()
        print
        print 'Keymap'
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
                    self.tup = (0,0)
                elif c == 8:
                    self.tup = (0,1)
                elif c == 9:
                    self.tup = (0,2)
                elif c == 4:
                    self.tup = (1,0)
                elif c == 5:
                    self.tup = (1,1)
                elif c == 6:
                    self.tup = (1,2)
                elif c == 1:
                    self.tup = (2,0)
                elif c == 2:
                    self.tup = (2,1)
                elif c == 3:
                    self.tup = (2,2)
                else:
                    raise ValueError
            except ValueError:
                print 'Please enter a valid number'
                continue
            finally:
