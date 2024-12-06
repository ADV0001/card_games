import pygame

"""
"""
''' CARD AND DECK SECTION  '''
class Card:

    def __init__(self,suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val,self.suit))

class Deck:
    suits = ["Spades","Clubs","Diamonds","Hearts"]
    numTochar_dict = {"1":"A","11":"J","12":"Q","13":"K"}
    START = 1
    STOP = 14
    def __init__(self):
        self.cards = []

    def build(self):
        for s in self.suits:
            for v in range(self.START,self.STOP):
                if str(v) in self.numTochar_dict.keys():
                    self.cards.append(Card(s,self.numTochar_dict[str(v)]))
                else:
                    self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def draw(self):
        pass

'''END OF CARD AND DECK SECTION  '''

'''CREATE PLAYING BOARD '''
class Board:
    GREEN = (0,250,0)
    WIDTH, HEIGHT = 400,400
    MARGIN = 5

    def __init__(self):
        pygame.init()
        window_size = [500,500]
        scr = pygame.display.set_mode(window_size)

    '''CREATE SECTION TO DRAW INITIAL BOARD '''


    '''CREATE SECTION FOR DECK AND DISCARD PILE '''

    '''CREATE SECTIONS FOR BOOKS/MATCHES '''



'''END OF BOARD CODE '''

#deck1 = Deck()
#deck1.build()
#deck1.show()
main_board = Board()
