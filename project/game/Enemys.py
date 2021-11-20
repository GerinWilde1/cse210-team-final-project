import arcade
import constants
from Moving_Object import Flying_Object
import Position
from constants import BIG_BOAT_SPEED, SCREEN_WIDTH
import math



class Enemys(Flying_Object):
    """Hols all the information for the enemy"""

    def __init__(self):

        super().__init__()
        # self.point = Position.Point()
        # self.velocity = Position.Velocity()

        self.bspeed = constants.BIG_BOAT_SPEED

        # self.velocity.dy = math.sin(math.radians(self.angle)) * self.bspeed


class Big_Boat(Enemys):
    """Build a Big_Boat on screen"""

    def __init__(self):

        super().__init__()
        self.center.y = 0
        self.center.x = 0

    def draw(self):
        """Draws th ebig boat"""

        arcade.draw.rectangle(self.center.x, self.center.y, constants.ENEMY_SHIPS_WIDTH, constants.ENEMY_SHIPS_HEIGHT, arcade.color.AERO_BLUE)

    def advance(self):
        """moves the Big_Boats if that's what we want for it to do"""

        super().advance()
        super().is_offscreen

    def hit (self):
        """Sets alive to False which will remove the boat from the game"""

        self.alive = False

# class Medium_Boat():
# class Small_boat():