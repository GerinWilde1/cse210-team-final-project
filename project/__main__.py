from game.Game import Game
import project.game.constants
import arcade


game = Game()
c = project.game.constants


window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
arcade.run()
# def main(screen):
#     pass

# if __name__ == "__main__":
#     main()