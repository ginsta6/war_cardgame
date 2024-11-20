from deck import Deck

def main():
    main_deck = Deck(full=False)
    print(main_deck.cards)

    player, cpu = main_deck.deal_cards()

    print("-------")
    print(player)
    print("-------")
    print(cpu)


if __name__ == "__main__":
    main()