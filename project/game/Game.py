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

    def on_draw(self):

    def update(self, delta_time):

    def create_ships(self):

    def check_collisions(self):

    def cleanup_zombies(self):

    def break_apart(self):

    def draw_gameover(self):
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