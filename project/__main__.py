from game.Game import Game
import game.constants
import arcade


game = Game()
c = game.constants


window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
arcade.run()
# def main(screen):
#     pass

# if __name__ == "__main__":
#     main()