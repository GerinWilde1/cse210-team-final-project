import arcade
from arcade.gui.widgets import UIFlatButton
from game.Game import Game
import game.constants as c
import arcade.gui



# class StartButton(arcade.gui.UIFlatButton):
#     def on_click(self, event: arcade.gui.UIOnClickEvent):
#         game_view = Game()
#         self.window.show_view(game_view)
#         game_view.setup()

# class StartView(arcade.View):

#     def __init__(self):
#         super().__init__(800, 600, "UIFlatButton Example", resizable=True)


#     def on_show(self):
#         """This id run once we switch to this view"""
#         self.background = arcade.load_texture("project/game/black_hole.jpg")
#         # arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        
#         # Reset the viewport, necessaey if we have a scrolling game and we need
#         # to reset the viewport back to the start do we can see what we draw
#         arcade.set_viewport(0, self.window.width, 0, self.window.height)


#     def on_draw(self):
#         """Draw this View"""
#         arcade.start_render()
#         arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2, self.window.width, self.window.height, self.background)
#         # Draws opening words to screen
#         arcade.draw_text("Opening Screen", self.window.width / 2, self.window.height / 2, arcade.color.DARK_SLATE_BLUE, font_size=50, anchor_x="center")
#         arcade.draw_text("Click to Advance", self.window.width / 2, self.window.height / 2-75, arcade.color.DARK_SLATE_BLUE, font_size=20, anchor_x="center")


#     def on_mouse_press(self, _x, _y, _button, _modifiers):
#         """on mouse press start game"""
#         game_view = Game()
#         self.window.show_view(game_view)
#         game_view.setup()

#     def set_restart(self):
#         game_view = Game()
#         self.window.show_view(game_view)
#         game_view.setup()


# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class StartView(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        @settings_button.event("on_click")
        def on_click_settings(event):
            print("Settings:", event)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    def setup(self):
        pass
    
    def on_click_start(self, event: arcade.gui.UIOnClickEvent):
        
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()
        
        # print("Start:", event)

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()






