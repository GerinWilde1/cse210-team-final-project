import arcade
import arcade.gui
import game.constants as c

class Instruction_View(arcade.View):

    def __init__(self, game_view):

        self.game_view = game_view

        self.background = arcade.load_texture(c.PATH + "/old_brick_wall.jpg")

        self.v_box = arcade.gui.UIBoxLayout()


    def on_show(self):
        """Show the intructions view"""
        
        # Adds manager for buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        back_button = arcade.gui.UIFlatButton(text="Back", width=200)

        back_button.on_click = self.on_click_back_button



    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)


        arcade.draw_taxt("How to play", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_taxt("Use the right and left arrows to move", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=16, anchor_x="center")
        arcade.draw_taxt("Hit the Space bar to shoot", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 400, arcade.color.WHITE, font_size=16, anchor_x="center")
        arcade.draw_taxt("Don't get Hit", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 450, arcade.color.WHITE, font_size=16, anchor_x="center")

        self.manager.draw()

    def on_click_back_button(self, event):

        self.game_view.setup()
        self.window.show_view(self.game_view)


