from game import Game
import sys

def main():
    try:
        if len(sys.argv) != 3:
            sys.exit("\033[95m Specify deck size (F/H) and round quantity \033[0m")
        else:
            match sys.argv[1].lower():
                case "f":
                    mygame = Game(True, int(sys.argv[2]))
                case "h":
                    mygame = Game(False, int(sys.argv[2]))
    except Exception as err:
        print(type(err))
    mygame.game_loop()


if __name__ == "__main__":
    main()