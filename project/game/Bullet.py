import constants
from Moving_Object import Flying_Object
import arcade
import math



class Bullet(Flying_Object):
    def __init__(self, center_x, center_y, velocity_x, velocity_y):
        """
            All the first info needed to create the Bullet
        """
        super().__init__()
        self.center.x = center_x
        self.center.y = center_y
        self.radius = constants.BULLET_RADIUS
        self.velocity.dx = velocity_x
        self.velocity.dy = velocity_y
        self.angle = 90
        self.life =  28
        self.alive = True
    def draw(self):
        """
        drawing the bullet
        """
        
        img2 = ":resources:images/space_shooter/laserBlue01.png"
        texture = arcade.load_texture(img2)
        width = texture.width
        height =  texture.height
        arcade.draw_texture_rectangle(self.center.x, self.center.y, width, height, texture, self.angle)
        
    def move(self):
        """
        all the bullets trig info so it knows how to set it in a straight line
        """
        if self.alive:
            # self.center.x += constants.BULLET_SPEED
            self.center.y += constants.BULLET_SPEED
        self.life -= 1