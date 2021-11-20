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
    """All the logic behind the game"""

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

    def create_ships(self):
        """builds the Big_Boats"""

        self.enemy_ships = Big_Boat()

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

    def draw_gameover(self):
<<<<<<< HEAD
        """

            Draws game over in the middle of the screen when Ship dies

        """

        text = "GAME OVER"

        start_x = 90

        start_y = 275

        arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=100,color=arcade.color.RED)

    def check_keys(self):
        """

            This function checks for keys that are being held down.

            You will need to put your own method calls in here.

        """

        

        if arcade.key.LEFT in self.held_keys:

            self.ship.turn_left()



        if arcade.key.RIGHT in self.held_keys:

            self.ship.turn_right()



        if arcade.key.UP in self.held_keys:

            self.ship.speed_up()



        if arcade.key.DOWN in self.held_keys:

            self.ship.slow_down()



        # Machine gun mode...

        if arcade.key.SPACE in self.held_keys:

            #bullet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy, self.ship.angle)

            #self.bullets.append(bullet)

            pass


    def on_key_press(self, key: int, modifiers: int):
  
        if self.ship.alive:

            self.held_keys.add(key)

            if key == arcade.key.SPACE:

                bullet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.velocity.dx, self.ship.velocity.dy, self.ship.angle)

                self.bullets.append(bullet)

                # TODO: move the bullet here!

                #self.bullet.move()

    def on_key_release(self, key: int, modifiers: int):
        """

            Removes the current key from the set of held keys.

        """
        if key in self.held_keys:

            self.held_keys.remove(key)
=======
        """once player is dead it desplays death message"""

    def check_keys(self):
        """
            This function checks for keys that are being held down.
            You will need to put your own method calls in here.
        """
    def on_key_press(self, key: int, modifiers: int):
        """
            Puts the current key in the set of keys that are being held.
            You will need to add things here to handle firing the bullet.
        """
    def on_key_release(self, key: int, modifiers: int):
        """
            Removes the current key from the set of held keys.
        """
>>>>>>> 6f80237734c72f68ba5a476d9d2d98d21488f27b
