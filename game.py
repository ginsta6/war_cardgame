from deck import Deck
class Game:
    def __init__(self):
        self._round = 0
        self._main_deck = Deck(full=False)
        self.player, self.cpu = self._main_deck.deal_cards()

    def game_loop(self):
        while True:
            self._round += 1
            self.game_round()

    def game_round(self):
        player_card = self.player.remove_card()
        cpu_card = self.cpu.remove_card()
        outcome = player_card.compare(cpu_card)
        if outcome == 0:
            #war
            ...
        elif outcome > 0:
            #player wins
            self.round_outcome([player_card, cpu_card], self.player)
        elif outcome < 0:
            #cpu wins
            self.round_outcome([player_card, cpu_card], self.cpu)

    def round_outcome(self, cards, winner: Deck):
        for card in cards:
            winner.add_card(card)

        
