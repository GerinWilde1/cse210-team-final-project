import arcade
import arcade.gui
import game.constants as c

class Instruction_View(arcade.View):

    def __init__(self, game_view):
        super().__init__()

        self.game_view = game_view

        self.background = arcade.load_texture(c.PATH + "/old_brick_wall.jpg")

        self.v_box = arcade.gui.UIBoxLayout()
        


        """Show the intructions view"""

        
        # Adds manager for buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        back_button = arcade.gui.UIFlatButton(text="Back", width=200)
        self.v_box.add(back_button.with_space_around(bottom= 20))
        back_button.on_click = self.on_click_back_button


        self.manager.add(arcade.gui.UIAnchorWidget(
         anchor_x = 'center_x',
         anchor_y = 'center_y',
         align_y = -200,
         child = self.v_box)
         )




    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)

        arcade.draw_text("How to play", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 200, arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Use the right and left arrows to move", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 300, arcade.color.WHITE, font_size=16, anchor_x="center")
        arcade.draw_text("Hit the Space bar to shoot", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 350, arcade.color.WHITE, font_size=16, anchor_x="center")
        arcade.draw_text("when one is destroied 2 will replace it", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 400, arcade.color.WHITE, font_size=16, anchor_x="center")        
        arcade.draw_text("Don't get Hit", c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT - 450, arcade.color.WHITE, font_size=16, anchor_x="center")
        

        self.manager.draw()

    def on_click_back_button(self, event):

        self.game_view.setup()
        self.window.show_view(self.game_view)


