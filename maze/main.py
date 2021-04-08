from controllers.game import GameController

def main():
    game = GameController()
    replay = game.run()
    if replay is True:
        main()

if __name__ == "__main__":
    main()
