import arcade
import constants
from Moving_Object import Flying_Object
import Position
from constants import BIG_BOAT_SPEED, SCREEN_WIDTH
import math
import random


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
        self.center.x = random.randint(5, constants.SCREEN_WIDTH - 10) 
        self.center.y = random.randint(constants.SCREEN_HEIGHT/2, constants.SCREEN_HEIGHT)
        self.radius = constants.ENEMY_SHIPS_RADIUS
        self.angle = 0

    def draw(self):
        """Draws th ebig boat"""
        img = ":resources:images/enemies/saw.png"
        texture = arcade.load_texture(img)
        angle = self.angle
        width = (texture.width/2) - 20
        height = (texture.height/2) - 20
        alpha = 255
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, angle, alpha)

    def advance(self):
        """moves the Big_Boats if that's what we want for it to do"""

        super().advance()
        super().is_offscreen

    def hit (self):
        """Sets alive to False which will remove the boat from the game"""

        self.alive = False

# class Medium_Boat():
# class Small_boat():