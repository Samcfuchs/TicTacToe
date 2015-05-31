# Human Player program end
from interface import *

class Human:
    """interface for a human player"""
    def __init__(self, player):
        #super(Human, self).__init__()
        # properties here to test access from other objects
        self.test = [1,2,3]
        self.num = 1
        self.keymap = [7,8,9,4,5,6,1,2,3] # matches numpad on keyboard
        self.choice = None
        self.player = player
        self.print_player()
        if input('Set a keymap? (0/1) '):
            self.set_keymap()
        else:
            self.print_keymap()

    def set_keymap():
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
        self.choice = input('Pick a square: ')
        try:
            if keymap.index(self.choice) == 1:
                choice = (0,0)
        except ValueError:
            print "That's not in the keymap"
