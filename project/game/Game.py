import constants
import Position
import Moving_Object
import Enemys
import Your_Ship
import math
import arcade
import os
import random

from project.game.Enemys import Big_Boat



class Game(arcade.Window):

    def __init__(self, width, height):


        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()


        self.ship = Your_Ship.Ship()
        self.bullets = []
        self.enemy_ships = []





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

    def create_ships(self):

        self.enemy_ships = Big_Boat()

    def check_collisions(self):

        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

    def cleanup_zombies(self):
         
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

    # def break_apart(self):

    def draw_gameover(self):

    def check_keys(self):

    def on_key_press(self, key: int, modifiers: int):

    def on_key_release(self, key: int, modifiers: int):