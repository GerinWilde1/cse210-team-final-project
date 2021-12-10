
import game.constants
import arcade
from Start_screen import StartView
from Start_screen2 import StartView2


# game = Game()
# c = project.game.constants


# window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
# arcade.run()
def main():
    

    window = arcade.Window(game.constants.SCREEN_WIDTH, game.constants.SCREEN_HEIGHT, game.constants.SCREEN_TITLE)
    start_view = StartView2()
    window.show_view(start_view)
    song = arcade.sound.load_sound("project/game/sound.mp3")
    arcade.sound.play_sound(song)

    # start_view.setup()
    arcade.run()

if __name__ == "__main__":
    main () 