import arcade
import constants
import Moving_Object
import Position
from project.game.constants import BIG_BOAT_SPEED
import math



class Enemys(Moving_Object):
    """Hols all the information for the enemy"""

    def __init__(self):

        super().__init__()
        self.point = Position.Point()
        self.velocity = Position.Velocity()

        self.bspeed = constants.BIG_BOAT_SPEED

        self.velocity.dy = math.sin(math.radians(self.angle)) * self.bspeed


class Big_Boat(Enemys):
    """Build a Big_Boat on screen"""

    def __init__(self):

        super().__init__()

    def draw(self):
        """Draws th ebig boat"""

        arcade.draw.rectangle(constants.ENEMY_SHIPS_WIDTH, constants.ENEMY_SHIPS_HEIGHT)

    def advance(self):
        """moves the Big_Boats if that's what we want for it to do"""

        super().advance()
        super().is_offscreen

    def hit (self):
        """Sets alive to False which will remove the boat from the game"""

        self.alive = False

# class Medium_Boat():
# class Small_boat():