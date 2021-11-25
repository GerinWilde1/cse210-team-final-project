from game.Game import Game
import game.constants
import arcade
from Instruction_screen import InstrustionView



# game = Game()
# c = project.game.constants


# window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
# arcade.run()
def main():
    

    window = arcade.Window(game.constants.SCREEN_WIDTH, game.constants.SCREEN_HEIGHT, game.constants.SCREEN_TITLE)
    start_view = InstrustionView()
    window.show_view(start_view)
    # start_view.setup()
    arcade.run()

if __name__ == "__main__":
    main()