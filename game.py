from deck import Deck
from card import Card
class Game:
    def __init__(self,full_deck: bool, max_rounds= 100):
        self._round = 0
        self._max_rounds = max_rounds
        self._main_deck = Deck(full_deck)
        self.player, self.cpu = self._main_deck.deal_cards()

    def game_loop(self):
        while True:
            self._round += 1
            if self._round > self._max_rounds:
                break
            if self.game_round():
                break
            print(f"Score:\nPlayer - {len(self.player.cards)} : {len(self.cpu.cards)} - CPU")
            if not self.continue_game():
                break
        print(f"{self.get_game_winner()} has won the game!")

    def get_game_winner(self):
        if len(self.player.cards) > len(self.cpu.cards):
            return "Player"
        elif len(self.player.cards) < len(self.cpu.cards):
            return "Your opponent"
        else:
            return "It's a tie!"
     

    def game_round(self):
        try:
            player_card = self.player.remove_card()
            cpu_card = self.cpu.remove_card()
        except IndexError:
            print("Not enought cards! Game over!")
            return True
        
        print(f"Round: {self._round}")
        print(f"Player plays {player_card}")
        print(f"CPU plays {cpu_card}")

        if winner := self.declare_winner([player_card], [cpu_card]):
            print(f"{winner} won the round!")
            return False
        else:
            return True

    def continue_game(self):
        while True:
            try:
                user_input = input("Press 'p' to play a card or 'q' to quit: ")
                if user_input.lower() == 'p':
                    return True
                elif user_input.lower() == 'q':
                    return False
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input! Please try again.")

    def declare_winner(self, player_pile: list[Card], cpu_pile: list[Card]):
        outcome = player_pile[-1].compare(cpu_pile[-1])
        if outcome == 0:
            #war
            return self.war_round(player_pile, cpu_pile)
        elif outcome > 0:
            #player wins
            self.round_outcome(player_pile + cpu_pile, self.player)
            return "You"
        elif outcome < 0:
            #cpu wins
            self.round_outcome(player_pile + cpu_pile, self.cpu)
            return "Your opponent"


    def war_round(self, player_pile: list[Card], cpu_pile: list[Card]):
        print("War has occured!")
        for _ in range(1):
            try:
                player_pile.append(self.player.remove_card())
                cpu_pile.append(self.cpu.remove_card())
            except IndexError:
                print("Not enough cards for a war! Game over!")
                return
        
        print(f"Player plays {player_pile[-1]}")
        print(f"CPU plays {cpu_pile[-1]}")
        return self.declare_winner(player_pile, cpu_pile)
        

    def round_outcome(self, cards: list[Card], winner: Deck):
        for card in cards:
            winner.add_card(card)

        
