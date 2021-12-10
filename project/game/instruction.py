import arcade
import project.game.constants as c
import arcade.gui
import os

class Instruction_View(arcade.View):

    def __init__(self, start_view):

        self.start_view = start_view

        self.background = False

        self.v_box = arcade.gui.UIBoxLayout()


    def on_show(self):
        """Show the intructions view"""
        
        # Adds manager for buttons
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        back_button = arcade.gui.UIFlatButton(text="Back", width=200)

        back_button.on_click = self.on_click_back_button



    def on_draw(self):
        return super().on_draw()


    def on_click_back_button(self, event):

        self.start_view.setup()
        self.window.show_view(self.start_view)


