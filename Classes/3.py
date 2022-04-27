import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
        
    def show(self):
        if self.value == 1:
            val = "A"
        elif self.value == 11:
            val = "J"
        elif self.value == 12:
            val = "Q"
        elif self.value == 13:
            val = "K"
        else:
            val = self.value

        return (f"{val} of {self.suit}")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for card in self.cards:
            print (card.show())

    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    def shuffle(self,):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        print(f"Hi! My name is {self.name}")

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    def showHand(self):
        print(f"{self.name}'s hand: {self.hand}")
        return self

    def discard(self):
        return self.hand.pop()


deck = Deck()
#deck.show()
deck.shuffle()
deck.show()

player = Player("Dhanaraj")

player.draw(deck, 2)
player.showHand()