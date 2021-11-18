import arcade
import constants
import Moving_Object
import Position
from project.game.Moving_Object import Flying_Object
from project.game.constants import BIG_BOAT_SPEED
import math


class Ship(Flying_Object):

    def __init__(self):
        super().__init__()


    def draw(self):

        arcade.draw_rectangle_filled(constants.SHIP_WIDTH, constants.SHIP_HEIGHT)

    # def move_right(self):

    # def move_left(self):