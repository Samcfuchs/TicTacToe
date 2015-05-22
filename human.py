# Human Player program end
from interface import *

class Human(Player):
    """interface for a human player"""
    def __init__(self):
        #super(Human, self).__init__()
        self.keymap = [7,8,9,4,5,6,1,2,3] # matches numpad on keyboard
        self.choice = None
        if input('Set a keymap? (0/1) '):
            self.set_keymap()
        else:
            self.print_keymap()

    def set_keymap():
        pass
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

    def turn():
        print 'Board'
        Game.print_board()
        print
        print 'Keymap'
        self.print_keymap()
        print
        self.choice = input('Pick a square: ')
        try:
            keymap.index(self.choice)
        except ValueError:
            print "That's not in the keymap"
