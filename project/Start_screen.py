import arcade
from game.Game import Game
import game.constants as c


class StartView(arcade.View):


    def on_show(self):
        """This id run once we switch to this view"""
        self.background = arcade.load_texture("project/game/black_hole.jpg")
        # arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        
        # Reset the viewport, necessaey if we have a scrolling game and we need
        # to reset the viewport back to the start do we can see what we draw
        arcade.set_viewport(0, self.window.width, 0, self.window.height)


    def on_draw(self):
        """Draw this View"""
        arcade.start_render()
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, self.window.width, self.window.height, self.background)
        # Draws opening words to screen
        arcade.draw_text("Opening Screen", self.window.width / 2, self.window.height / 2, arcade.color.DARK_SLATE_BLUE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75, arcade.color.DARK_SLATE_BLUE, font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """on mouse press sart game"""
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()

    def set_restart(self):
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()



