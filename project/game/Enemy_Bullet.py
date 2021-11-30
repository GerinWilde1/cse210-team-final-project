import arcade
import game.Bullet
from game.Bullet import Bullet as Bullet
from game.Enemys import Big_Boat as enemy_ship
import game.Game



class Enemy_bullet(Bullet):

    def __init__(self):
        super().__init__()
        self.shoot_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.bullet = game.Bullet()
        
    def enemy_shoot(self):
                
                Bullet (enemy_ship.center.x, enemy_ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy)
                arcade.play_sound(self.shoot_sound)