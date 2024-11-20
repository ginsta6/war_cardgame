from card import Card
from random import shuffle

class Deck:
    def __init__(self, full:bool = None):
        self._cards = []
        if full is True:
            self._add_full_deck()
        elif full is False:
            self._add_high_deck()
    
    @property
    def cards(self):
        return self._cards
    
    def add_card(self, card:Card):
        self.cards.append(card)

    def remove_card(self):
        return self.cards.pop()
    
    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_cards(self):
        first = Deck()
        second = Deck()
        self.shuffle_deck()
        for _ in range(int(len(self.cards) / 2)):
            first.add_card(self.cards.pop())
            second.add_card(self.cards.pop())

        return first, second

    def _add_full_deck(self):
        for suit in Card.SUIT_VALUES:
            for rank in Card.RANK_VALUES:
                self.add_card(Card(suit, rank))

    def _add_high_deck(self):
        for suit in Card.SUIT_VALUES:
            start = False
            for rank in Card.RANK_VALUES:
                if rank == "9":
                    start = True
                if start:
                    self.add_card(Card(suit,rank))

    def __str__(self):
        return self.cards.__str__()


    