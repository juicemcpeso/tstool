#!/usr/bin/python3

from CardGame import *

class TwilightStruggleCard(Card):
    """Class of cards specific to the game Twilight Struggle"""
    
    def __init__(self, n, no, p, e, o, r, opt):
        Card.__init__(self, n) 
        
        if (not no.isdigit()):
            raise ValueError("Error creating Twilight Struggle Card. Number parameter must be a number.")
        self.number = int(no)
        
        if (p not in ['early war', 'mid war', 'late war']):
            raise ValueError("Error creating Twilight Struggle Card. Period parameter must be one of: 'early war', 'mid war', 'late war'.")
        self.period = p 

        if (e not in ['scoring', 'us', 'ussr', 'neutural']):
            raise ValueError("Error creating Twilight Struggle Card. Event parameter must be one of: 'scoring', 'us', 'ussr', 'neutural'.")
        self.event = e
        
        if (not o.isdigit() and (int(o) > 4 or int(o) < 1)):
            raise ValueError("Error creating Twilight Struggle Card. Ops parameter must be a number between 1 and 4 inclusively.")
        self.ops = int(o)

        if (not r.isdigit() and int(r) != 1 and int(r) != 0):
            raise ValueError("Error creating Twilight Struggle Card. Removed parameter must be a 1 or a 0.")
        self.removed = True if int(r) == 1 else False

        if (not opt.isdigit() and int(opt) != 1 and int(opt) != 0):
            raise ValueError("Error creating Twilight Struggle Card. Optional parameter must be a 1 or a 0.")
        self.optional = True if int(opt) == 1 else False
       
class TwilightStruggleGame(CardGame):
    """Class of an individual game of Twilight Struggle"""
    
    turns = 10
    action_rounds = {1:6,2:6,3:6,4:7,5:7,6:7,7:7,8:7,9:7,10:7}

    def __init__(self, n, d, opt):
        CardGame.__init__(self, n, d)

        if (not opt.isdigit() and int(opt) != 1 and int(opt) != 0):
            raise ValueError("Error creating Twilight Struggle Game. Optional cards parameter must be a 1 or a 0.")
        self.optional_cards = True if opt == 1 else False

        self.__create_piles()
        self.__create_cards()

    def __create_cards(self):
        with open("cards/card_list.csv", "r") as handle:
            header = handle.readline()
            lines = handle.read().splitlines()

        for line in lines:
            card = TwilightStruggleCard(*line.split(","))
            if (not self.optional_cards and card.optional):
                continue
            start_pile = self.get_pile(card.period)
            if (not start_pile):
                raise ValueError("Error adding card " + str(card) + " to pile " + str(start_pile) + ".")
            start_pile.add_card(card)

    def __create_piles(self):
        with open("piles/pile_list.csv", "r") as handle:
            header = handle.readline()
            lines = handle.read().splitlines()

        for line in lines:
            self.add_pile(CardPile(*line.split(",")))

def main():
    game = TwilightStruggleGame("default_name","03/04/28","0")
    for turn in range(1,game.turns+1):
        #headline
        print("Turn %d Headline!" % (turn))

        #action rounds
        for ar in range(1,game.action_rounds[turn]+1):
            print("Turn %d, AR %d!" % (turn, ar))

if __name__ == "__main__":
    main()
