
import game.constants as constants
import game.Position as Position
class Flying_Object:
    
    def __init__(self):
        """
            All of the info needed to cary into all the other everything else
        """
        self.center = Position.Point(0.0,0.0)
        self.velocity = Position.Velocity(0.0,0.0)

        self.alive = True

        
    def advance(self):
        """
            For movement
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def is_offscreen(self):
        """Lets the computer know if the item is off screem and needs to be removed"""
        if self.center.x > constants.SCREEN_WIDTH:
            self.center.x = 0.0
        if self.center.y > constants.SCREEN_HEIGHT:
            self.center.y = 0.0
        if self.center.x < 0.0:
            self.center.x = constants.SCREEN_WIDTH
        if self.center.y < 0.0:
            self.center.y = constants.SCREEN_HEIGHT