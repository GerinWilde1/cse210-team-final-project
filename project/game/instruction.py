import arcade
from arcade.color import BLACK, WHITE
import game.constants as c
import os

class Instruction_View(arcade.View):
    """View that get's shown once the game is over"""
    def __init__(self, game_view):
        """This is run once the player dies/we switch to this view"""
        super().__init__()
        
        # self.background = arcade.load_texture("")

        # Reset the viewport, necessaey if we have a scrolling game and we need
        # to reset the viewport back to the start do we can see what we draw
        arcade.set_viewport(0, self.window.width - 1, 0, self.window.height - 1)

        self.screen_width = c.SCREEN_WIDTH
        self.screen_height = c.SHIP_HEIGHT

        self.right = arcade.load_texture(":resources:onscreen_controls/shaded_dark/right.png")
        self.left = arcade.load_texture(":resources:onscreen_controls/shaded_dark/left.png")
        self.space = arcade.draw_rectangle_outline(30, 10, WHITE)


        

    def on_draw(self):
        """Draw this View"""
        arcade.start_render()
        #sets backbround image
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, self.window.width, self.window.height, BLACK)
        #draws text on screen
        arcade.draw_text("Instruction Screen", self.window.width / 2, self.window.height / 2 + 75, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(f"{self.right} Move Right", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(f"{self.left} Move Left", self.window.width / 2, self.window.height / 2 - 10, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text(f"{self.space} To Shoot", self.window.width / 2, self.window.height / 2 - 10, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to start", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")



    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """on mouse press start game"""
        from game.Game import Game
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()