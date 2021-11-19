import arcade
import constants
import Moving_Object
import Position
from project.game.constants import BIG_BOAT_SPEED
import math



class Enemys(Moving_Object):

    def __init__(self):

        super().__init__()
        self.point = Position.Point()
        self.velocity = Position.Velocity()

        self.bspeed = constants.BIG_BOAT_SPEED

        self.velocity.dy = math.sin(math.radians(self.angle)) * self.bspeed


class Big_Boat(Enemys):

    def __init__(self):

        super().__init__()

    def draw(self):

        arcade.draw.rectangle(constants.ENEMY_SHIPS_WIDTH, constants.ENEMY_SHIPS_HEIGHT)

    def advance(self):

        super().advance()
        super().is_offscreen

    def hit (self):

        self.alive = False

# class Medium_Boat():
# class Small_boat():