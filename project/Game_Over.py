import arcade
import game.constants

class Game_Over(arcade.View):
    """View that get's shown once the game is over"""
    def __init__(self):
        """This is run once the player dies/we switch to this view"""
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")


        # Reset the viewport, necessaey if we have a scrolling game and we need
        # to reset the viewport back to the start do we can see what we draw
        arcade.set_viewport(0, self.window.width - 1, 0, self.window.height - 1)

        self.screen_width = game.constants.SCREEN_WIDTH
        self.screen_height = game.constants.SHIP_HEIGHT


    def on_draw(self):
        """Draw this View"""
        arcade.start_render()
        arcade.draw_text(self.screen_width, self.screen_height, self.screen_width / 2, self.screen_height / 2)



    def on_mouse_press(self, _x, _y, _button, _modifiers):
        
        game_view = game.Game()
        game_view.setup()
        self.window.show_view(game_view)