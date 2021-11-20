import math 

class Velocity:
    """
        Keeps track of the motion of the item
    """
    def __init__(self, init_dx, init_dy):
        self.dx = init_dx
        self.dy = init_dy

    

    def speed_up(self):

        """

            When the up button is pressed this moves the ship forward

        """

        self.velocity.dy += math.cos(math.radians(self.angle)) * self.thrust

        self.velocity.dx -= math.sin(math.radians(self.angle)) * self.thrust

        

    def slow_down(self):

        """

            When the down button is pressed this moves the ship backward

        """

        self.velocity.dy -= math.cos(math.radians(self.angle)) * self.thrust

        self.velocity.dx += math.sin(math.radians(self.angle)) * self.thrust
