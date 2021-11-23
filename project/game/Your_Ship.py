import arcade
import game.constants
# import Moving_Object
# import Position
from game.Moving_Object import Flying_Object
import math

constants = game.constants
class Ship(Flying_Object):
    """The class for the player's ship"""
    def __init__(self):

        super().__init__()
        self.center.x = constants.SCREEN_WIDTH // 2
        self.center.y = constants.SCREEN_HEIGHT - 550
        self.angle = 0
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover4.wav")
        # self.advance = Flying_Object.advance(self)


    def draw(self):
        """Draws the Player's ship in the corner"""

        img = ":resources:images/space_shooter/playerShip1_orange.png"
        texture = arcade.load_texture(img)
        
        width = texture.width/2
        height = texture.height/2
        alpha = 255
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.angle, alpha)

    def move_right(self):
        """Movers the player's ship right"""
        if self.center.x + (constants.SHIP_WIDTH/2) <= constants.SCREEN_WIDTH:
            self.center.x += 5


    def move_left(self):
        """moves the players ship left"""
        if self.center.x - (constants.SHIP_WIDTH/2) >= 0:
            self.center.x -= 5


    def hit(self):
        """If the player is hit it sets the players alive to false which will remove the player from the game."""
        arcade.play_sound(self.gameover_sound)
        self.alive = False


    

    # def turn_right(self):

    #     """

    #         When the right button is pressed this moves turns the ship right

    #     """

    #     self.angle += self.turn

    

    # def turn_left(self):

    #     """

    #         When the up button is pressed this turns the ship left

    #     """

    #     self.angle -= self.turn
