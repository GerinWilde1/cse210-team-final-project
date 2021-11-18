class Point:
    """
        Keeps track of where the item is located
    """
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y

class Velocity:
    """
        Keeps track of the motion of the item
    """
    def __init__(self, init_dx, init_dy):
        self.dx = init_dx
        self.dy = init_dy