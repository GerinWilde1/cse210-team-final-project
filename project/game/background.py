import arcade
import game.constants



constants = game.constants
class background():
    """The class for the background"""
    def __init__(self):   
        self.center = 400
        self.angle = 0


    def draw(self):
        """Draws the game background"""

        img = "project/game/lunar.jpg"
        texture = arcade.load_texture(img)
        
        width = texture.width *1.3
        height = texture.height*1.8
        alpha = 255
        arcade.draw_texture_rectangle(self.center, self.center, width, height, texture, self.angle, alpha)