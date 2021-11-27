import arcade
import game.constants
import game.Game
import os

class Game_Over(arcade.View):
    """View that get's shown once the game is over"""
    def __init__(self):
        """This is run once the player dies/we switch to this view"""
        super().__init__()
        
        self.background = arcade.load_texture("project/game/Roll.gif")

        # Reset the viewport, necessaey if we have a scrolling game and we need
        # to reset the viewport back to the start do we can see what we draw
        arcade.set_viewport(0, self.window.width - 1, 0, self.window.height - 1)

        self.screen_width = game.constants.SCREEN_WIDTH
        self.screen_height = game.constants.SHIP_HEIGHT


    def on_draw(self):
        """Draw this View"""
        arcade.start_render()
        #sets backbround image
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, self.window.width, self.window.height, self.background)
        #draws text on screen
        arcade.draw_text("GAME OVER", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to restart", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")



    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """on mouse press start the game over"""
        game_view = game.Game()
        self.window.show_view(game_view)
        game_view.setup()