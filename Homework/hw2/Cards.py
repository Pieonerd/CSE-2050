import random


class Deck:
    "Deck class"
    def __init__(self, values=range(1, 14), suits=['clubs','diamonds','hearts','spades'], card_list=[]):
        """Initlization function"""
        self.values = values
        self.suits = suits
        card_list = []
        for suit in self.suits:
            for value in self.values:
                card_list.append(Card(value, suit))
        self.card_list = card_list

    def __len__(self):
        """Returns length of deck"""
        return len(self.card_list)

    def sort(self):
        """Sorts the deck"""
        self.card_list = sorted(self.card_list)
        return self.card_list

    def __repr__(self):
        """String representation function"""
        return f'Deck: {self.card_list}'
    
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.card_list)
        return self.card_list
    
    def draw_top(self):
        """Returns the card last in the deck and removes it, raises a RunTimeError if card does not exist"""
        if not self.card_list:
            raise RuntimeError('Cannot draw from empty deck')

        return self.card_list.pop(-1)


class Hand(Deck):
    "Hand class"
    def __init__(self, card_list):
        """Initilization function"""
        Deck.__init__(self, card_list)
        self.card_list = card_list

    def __repr__(self):
        """String representation function"""
        return f'Hand: {self.card_list}'

    def play(self, card):   
        """Checks if appropriate card is in the deck, raises a RuntimeError if not"""     
        if card in self.card_list:
            self.card_list.remove(card)
            return card
        else:
            raise RuntimeError(f'Attempt to play {card} that is not in {self.card_list}')


class Card:
    "Card class"
    def __init__(self, value, suit):
        """Initialization function"""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """String representation function"""
        return f'Card({self.value} of {self.suit})'

    def __lt__(self, other):
        """Returns true if a card is less than other card"""
        if self.suit != other.suit:
            return self.suit < other.suit
        else:
            return self.value < other.value

    def __eq__(self, other):
        """Returns true if two cards are equal to each other"""
        if self.suit == other.suit:
            return self.value == other.value