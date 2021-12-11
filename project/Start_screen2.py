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
        instruction_button = arcade.gui.UIFlatButton(text="Instructions", width=200)
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)


        self.v_box.add(start_button.with_space_around(bottom=20))
        self.v_box.add(instruction_button.with_space_around(bottom=20))
        self.v_box.add(quit_button)

        start_button.on_click = self.on_click_start
        quit_button.on_click = self.on_click
        instruction_button.on_click = self.on_click_instruction


        self.manager.add(arcade.gui.UIAnchorWidget(
         anchor_x='center_x',
         anchor_y='center_y',
         child=self.v_box)
         )
        song = arcade.sound.load_sound("project/game/sound.mp3")
        arcade.sound.play_sound(song)

    def setup(self):
        pass
    
    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background)
        self.manager.draw()


    def on_click_start(self, event):
        
        game_view = Game()
        self.window.show_view(game_view)
        game_view.setup()

        print("Start: ", event)
    

    def on_click_instruction(self, event):
        view = InstructionScreen(self)
        self.window.show_view(view)

        print("Instructions:", event)





    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()







