import constants
import Position
import Moving_Object
import Enemys
import Your_Ship
import math
import arcade
import os
import random
from Enemys import Big_Boat
import Bullet



class Game(arcade.Window):
    """All the logic behind the game"""

    def __init__(self, width, height):


        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()


        self.ship = Your_Ship.Ship()
        self.bullets = []
        self.enemy_ships = []
        self.shipcount = constants.INITIAL_SHIP_COUNT




    def on_draw(self):

        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        # clear the screen to begin drawing
        arcade.start_render()
        
        
        

        
        for bullet in self.bullets:
            bullet.draw()
        
        if self.ship.alive:
            self.ship.draw()
        else:
            self.draw_gameover()

        
        
        for enemy in self.enemy_ships:
            enemy.draw()
            
             



    def update(self, delta_time):
        """Deals with all the updates. things like Movement, Collision, and bullet/ship info"""

        self.check_keys()
        self.check_collisions()

        self.ship.advance()
        self.ship.is_offscreen()

        for bullet in self.bullets:
            bullet.advance()

        for bullet in self.bullets:
            bullet.move()
            bullet.is_offscreen()
            if bullet.life == 0:
                self.bullets.remove(bullet)
        
        
        if self.shipcount != 0:
            self.create_ships()
            self.shipcount -= 1

    def create_ships(self):
        """builds the Big_Boats"""

        self.enemy_ship = Big_Boat()
        self.enemy_ships.append(self.enemy_ship)

    def check_collisions(self):
        """all the information to know if something has been shot"""
        for bullet in self.bullets:
            for enemys in self.enemy_ships:
                if bullet.alive and enemys.alive:
                    too_close = bullet.radius + enemys.center.x

                    if abs(bullet.center.x + self.enemy_ship.center.x) < too_close and abs(bullet.center.y + self.enemy_ship.center.y) < too_close:
                        enemys.hit()
                        bullet.alive = False
                        print("hit")

    def cleanup_zombies(self):
        """removed alive = False things from the game"""
         
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

    #def break_apart(self):

    def draw_gameover(self):
        """once player is dead it desplays death message"""
        
        text = "GAME OVER"
        start_x = 80
        start_y = 250
        arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=100,color=arcade.color.RED)

    def check_keys(self):
        """
            This function checks for keys that are being held down.
            You will need to put your own method calls in here.
        """

        if arcade.key.LEFT in self.held_keys:
            self.ship.move_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.move_right()


    def on_key_press(self, key: int, modifiers: int):
        """
            Puts the current key in the set of keys that are being held.
            You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet.Bullet (self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy)
                self.bullets.append(bullet)


    def on_key_release(self, key: int, modifiers: int):
        """
            Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


c = constants


window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
arcade.run()