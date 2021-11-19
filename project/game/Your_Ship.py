import arcade
import constants
import Moving_Object
import Position
from project.game.Moving_Object import Flying_Object
import math


class Ship(Flying_Object):

    def __init__(self):
        super().__init__()
        self.center.x = constants.SCREEN_WIDTH // 2
        self.center.y = constants.SCREEN_HEIGHT // 2


    def draw(self):

        arcade.draw_rectangle_filled(constants.SHIP_WIDTH, constants.SHIP_HEIGHT)

    # def move_right(self):

    # def move_left(self):

    def hit(self):

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
