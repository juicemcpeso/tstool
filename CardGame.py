class Card:
    """Base class for a generic card in a game"""
    
    def __init__(self, n):
        self.name = n

    def __repr__(self):
        return "<Card: %s>" % (self.name)

    def __str__(self):
        return self.name

class CardPile:
    """Base class for a collection of Card objects"""

    def __init__(self, n, card_list = []):
        self.name = n
        self.cards = []
        for card in card_list:
            self.add_card(card)

    def add_card(self, c):
        if (isinstance(c, Card)):
            self.cards.append(c)
        else:
            raise ValueError("Could not add card " + str(c) + " to card pile " + str(self) + ".")

    def remove_card(self, c):
        try:
            self.cards.remove(c)
        except ValueError:
            raise ValueError("Could not remove card " + str(c) + " from card pile " + str(self) + ".")

    def get_card(self, n):
        card = None
        card_list = list(filter(lambda x: x.name == n, self.cards))
        if (len(card_list)):
            card = card_list.pop()
        return card

    def get_pile_size(self):
        return len(self.cards)

    def __repr__(self):
        string = "<CardPile: %s>\n" % (self.name)
        for card in self.cards:
            string += "\t" + repr(card) + "\n"
        return string

    def __str__(self):
        return self.name

class CardGame:
    """Base class for a collection of CardPile objects"""
    
    def __init__(self, n, d):
        self.name = n
        self.date = d
        self.piles = []

    def add_pile(self, p):
        if (isinstance(p, CardPile)):
            self.piles.append(p)
        else:
            raise ValueError("Could not add pile " + str(p) + " to card game " + str(self.name) + ".")

    def remove_pile(self, p):
        try:
            self.piles.remove(p)
        except ValueError:
            raise ValueError("Could not remove pile " + str(p) + " from card game " + str(self.name) + ".")

    def get_pile(self, n):
        pile = None
        pile_list = list(filter(lambda x: x.name == n, self.piles))
        if (len(pile_list)):
            pile = pile_list.pop()
        return pile

    def __repr__(self):
        string = "<CardGame: %s on %s>" % (self.name, self.date)
        for pile in self.piles:
            string += "\t" + repr(pile) + "\n"
        return string

    def __str__(self):
        return "%s on %s" % (self.name, self.date)
