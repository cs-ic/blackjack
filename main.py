from itertools import product
from random import choice

class Card:
    def __init__(self,card):
        self.face = card[0]
        self.value = card[1]
        if self.value in "23456789":
            self.count = int(self.value)
        elif self.value == "1":
            self.count = 1 # add both 1 and 11 for it
        else:
            self.count = 10


class Deck:
    def __init__(self):
        faces = {"Ace","Diamond","Spade","Hearts"}
        value = {'1','2','3','4','5','6','7','8','9','10','J','Q','K'}
        self.deck = [i for i in product(*[faces, value])]

class Blackjack:
    def __init__(self):
        self.deck = Deck().deck
    
    def Pull(self):
        self.card = Card(choice(self.deck))
        return self.card

class Game(Blackjack):
    def __init__(self):
        self.players = {}
        self.deck = Blackjack().deck

    def play(self,player):
        self.players[player] = []
        while sum(self.players[player]) <= 21 and input("Draw a Card (Y/N) : ") == "Y":
            self.players[player].append(self.Pull().count)
            print(player, self.players[player])
        

a = Game().play("User")





