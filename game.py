from deck import Deck
class Game:
    def __init__(self):
        self._round = 0
        self._main_deck = Deck(full=False)
        self.player, self.cpu = self._main_deck.deal_cards()

    def start_game(self):
        ...