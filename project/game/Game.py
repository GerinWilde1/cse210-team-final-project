import constants
import Position
import Moving_Object
import Enemys
import Your_Ship
import math
import arcade
import os
import random



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

        
        
        for asteroid in self.asteroids:
            asteroid.draw()
            
             



    def update(self, delta_time):

    def create_ships(self):

    def check_collisions(self):

    def cleanup_zombies(self):

    # def break_apart(self):

    def draw_gameover(self):

    def check_keys(self):

    def on_key_press(self, key: int, modifiers: int):

    def on_key_release(self, key: int, modifiers: int):