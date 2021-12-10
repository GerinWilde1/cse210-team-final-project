import arcade
import arcade.gui
from game.Game import Game
import game.constants as c
from game.instruction import Instruction_View as InstructionScreen





class StartView2(arcade.View):


    def __init__(self):

        super().__init__()
        self.background = arcade.load_texture(c.PATH + "/black_hole.jpg")
        
        # self.music

        self.v_box = arcade.gui.UIBoxLayout()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        quit_button = QuitButton(text="Quit", width=200)
        # play_button = arcade.gui.UITextureButton(x=0, y=0, texture=arcade.load_texture(c.PATH + '/images/play.png'), texture_hovered=arcade.load_texture(c.PATH + '/images/play_hovered.png'), texture_pressed=arcade.load_texture(constants.PATH + '/images/play_pressed.png'), scale=constants.BUTTON_SCALING)


        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(settings_button.with_space_around(bottom=20))
        self.v_box.add(quit_button)

        start_button.on_click = self.on_click_start
        quit_button.on_click = quit_button


        self.manager.add(arcade.gui.UIAnchorWidget(
         anchor_x='center_x',
         anchor_y='center_y',
         child=self.v_box)
         )



    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        self.manager.draw()


    def on_click_start(self, event):
        
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()

        print("Start: ", event)
    

    def on_click(self, event: arcade.gui.UIOnClickEvent):
        game_view = InstructionScreen()
        self.window.show_view(game_view)
        game_view.setup()



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()




# class InstructionButton(arcade.gui.UIFlatButton):
#     def on_click(self, event: arcade.gui.UIOnClickEvent):
#         game_view = InstructionScreen()
#         self.window.show_view(game_view)
#         game_view.setup()


