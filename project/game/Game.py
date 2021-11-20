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

        # self.check_keys()
        # self.check_collisions()

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

    def check_collisions(self):
        """all the information to know if something has been shot"""
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

    def cleanup_zombies(self):
        """removed alive = False things from the game"""
         
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

    # def break_apart(self):

    # def draw_gameover(self):
    #     """once player is dead it desplays death message"""

    # def check_keys(self):
    #     """
    #         This function checks for keys that are being held down.
    #         You will need to put your own method calls in here.
    #     """
    # def on_key_press(self, key: int, modifiers: int):
    #     """
    #         Puts the current key in the set of keys that are being held.
    #         You will need to add things here to handle firing the bullet.
    #     """
    # def on_key_release(self, key: int, modifiers: int):
    #     """
    #         Removes the current key from the set of held keys.
    #     """

c = constants


window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
arcade.run()