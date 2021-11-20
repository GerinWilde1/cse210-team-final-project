import arcade
import constants
import Moving_Object
import Position
from Moving_Object import Flying_Object
import math


class Ship(Flying_Object):
    """The class for the player's ship"""
    def __init__(self):

        super().__init__()
        self.center.x = constants.SCREEN_WIDTH // 2
        self.center.y = constants.SCREEN_HEIGHT // 2


    def draw(self):
        """Draws the Player's ship in the corner"""
        arcade.draw_rectangle_filled(constants.SHIP_WIDTH, constants.SHIP_HEIGHT)

    def move_right(self):
        """Movers the player's ship right"""
        if self.center.x + (constants.SHIP_WIDTH/2) <= constants.SCREEN_WIDTH:
            self.center.x += 1


    def move_left(self):
        """moves the players ship left"""
        if self.center.x - (constants.SHIP_WIDTH/2) >= 0:
            self.center.x -= 1


    def hit(self):
        """If the player is hit it sets the players alive to false which will remove the player from the game."""

        self.alive = False


    

    def turn_right(self):

        """

            When the right button is pressed this moves turns the ship right

        """

        self.angle += self.turn

    

    def turn_left(self):

        """

            When the up button is pressed this turns the ship left

        """

        self.angle -= self.turn
