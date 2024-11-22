class Card:
    RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "jack": 11,
    "queen": 12,
    "king": 13,
    "ace": 14
    }

    SUIT_VALUES = ["spades", "clubs", "hearts", "diamonds"]

    def __init__(self, suit:str, rank:str):
        if suit.lower() not in Card.SUIT_VALUES:
            raise ValueError("Invalid card suit")
        self._suit = suit.lower().title()

        if rank.lower() not in Card.RANK_VALUES:
            raise ValueError("Invalid card rank")
        self._rank = rank.lower().title()

    @property
    def suit(self):
        return self._suit
    
    @property
    def rank(self):
        return self._rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
    def __repr__(self):
        return f"Rank:={self.rank} Suit:={self.suit}"
    
    def compare(self, other_card):
        ''' 0 if equal, negative if other is bigger, positive if self is bigger '''
        return Card.RANK_VALUES[self.rank.lower()]-Card.RANK_VALUES[other_card.rank.lower()]
    
