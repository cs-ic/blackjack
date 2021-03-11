from itertools import product
from random import choice

class Card:
    def __init__(self,card):
        self.face = card[0]
        self.value = card[1]
        if self.value in "23456789":
            self.count = int(self.value)
        elif self.value == "1":
            self.count = 11 # add both 1 and 11 for it
        else:
            self.count = 10


class Deck:
    def __init__(self):
        faces = {"Club","Diamond","Spade","Hearts"}
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

    def value(self,cards,show = True): # work out for Ace having value of 1 and 11, show for printing list
        self.player_values = [card.count for card in cards]

        while 11 in self.player_values and sum(self.player_values) > 21: 
            for i in range(len(self.player_values)):
                if self.player_values[i] == 11:
                    self.player_values[i] = 1 
                    break

        if show : print([card.value + " of " + card.face for card in cards])
        return sum(self.player_values)
            

    def play(self,player):
        self.players[player] = []
        while input(f"{player}, Draw a Card (Y/N) : ") == "Y":
            self.players[player].append(self.Pull())
            check = self.value(self.players[player])
            if check == 21:
                print("BlackJack!!!!!")
                break
            elif check > 21:
                print("Busted!!!!!!")
                break
        else:
            print(f"{player}, Card Count = ", check)
        
        return check
            

    
        
if __name__ == '__main__':
    a = Game().play("Player")
    print("\n")
    b = Game().play("House")

    print("\n*--------------*\n")
    if a > 21 and b > 21:
        print("Both Player Busted!!!, It's a Tie.")
    elif a == 21 and b == 21:
        print("Both Player Blackjacked!!!, It's a Tie.")
    elif a > 21 and b < 21:
        print("Player Busted!!!!, House Wins.")
    elif a < 21 and b > 21:
        print("House Busted!!!, Player Wins.")
    elif a > b:
        print("Player Wins!!!!")
    elif b > a:
        print("House Wins!!!!")
    else:
        print("Something Went Wrong!!!")
        print("Player = ", a)
        print("House  = ", b)

    print("\n")







