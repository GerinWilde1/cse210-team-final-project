from arcade.window_commands import schedule, set_background_color
import game.constants as constants
import game.Your_Ship as Your_Ship
# import math
import arcade
import game.Enemy_Bullet as Enemy_Bullet
import random
from game.Enemys import Big_Boat
import game.Bullet as Bullet
import Game_Over
import game.background as background

# from game.Enemy_Spawn import Enemy_Spawn



class Game(arcade.View):
    """All the logic behind the game"""

    def __init__(self):


        super().__init__()
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        self.ship = Your_Ship.Ship()
        self.bullets = []
        self.enemy_bullets = []
        self.enemy_ships = []
        
        self.shipcount = constants.INITIAL_SHIP_COUNT
        self.shoot_sound = arcade.load_sound(":resources:sounds/jump1.wav")
        self.ship_hit_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.background = background.Background()


    def on_draw(self):

        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        # clear the screen to begin drawing
        arcade.start_render()
        
        if self.ship.alive:
            self.background.draw()
            self.ship.draw()
        
        else:
             self.draw_gameover()

        
        for bullet in self.bullets:
            bullet.draw()
        


        
        
        for enemy in self.enemy_ships:
            enemy.draw()
            
    # def enemy_shoot(self, delta_time):
    #     shoot_time = random.randint (1, 3)
    #     if self.enemy_ship.alive:
    #         arcade.schedule(Enemy_Bullet, shoot_time)
    #         self.enemy_bullets.append(Bullet)

        
 




    def update(self, delta_time):
        """Deals with all the updates. things like Movement, Collision, and bullet/ship info"""

        self.check_keys()
        self.check_collisions()
        # Enemy_Spawn(self)
        self.spawn_ships
        self.ship.advance()
        self.ship.is_offscreen()
        
        

        for bullet in self.bullets:
            bullet.advance()
            bullet.move()
            if bullet.center.y == 0:
                self.bullets.remove(bullet)

        for enemy in self.enemy_ships:
            enemy.advance()
            enemy.is_offscreen()
            if enemy.center.y == constants.SCREEN_HEIGHT:
                self.enemy_ships.remove(enemy)
                # constants.INITIAL_SHIP_COUNT += 1
                # self.create_ships()
                # spawn_rate = random.randint(1, 3)
        
                # arcade.schedule(self.create_ships(), spawn_rate)

        
        if self.shipcount != 0:
            self.create_ships()
            self.shipcount -= 1

        # for bullet in self.enemy_bullets:
        #     bullet.advance()
        #     bullet.move()
        #     if bullet.center.y == constants.SCREEN_HEIGHT:
        #         self.enemy_bullets.remove(bullet)
        
    
    def setup(self):
        pass

    def create_ships(self):
        """builds the Big_Boats"""

        self.enemy_ship = Big_Boat()
        self.enemy_ships.append(self.enemy_ship)

    def spawn_ships(self):
        spawn_rate = random.randint(1, 3)
        
        arcade.schedule(self.create_ships(), random.randint(1, 3))

        

    def check_collisions(self):
        """all the information to know if something has been shot"""
        for bullet in self.bullets:
            for enemys in self.enemy_ships:
                if bullet.alive and enemys.alive:
                    too_close = bullet.radius + enemys.radius

                    if abs(bullet.center.x - enemys.center.x) < too_close and abs(bullet.center.y - enemys.center.y) < too_close:
                        enemys.hit()
                        bullet.alive = False
                        constants.INITIAL_SHIP_COUNT += 1
                        self.create_ships()

                        

        for enemy in self.enemy_ships:
            if enemy.alive and self.ship.alive:
                too_close = enemy.radius + self.ship.radius

                if (abs(enemy.center.x - self.ship.center.x) < too_close and abs(enemy.center.y - self.ship.center.y) < too_close):
                    self.ship.hit()
                    enemy.alive = False
                    view = Game_Over.Game_Over(self)
                    if self.ship.ship_lives == 0:
                        self.window.show_view(view)

        self.cleanup_zombies()

    def cleanup_zombies(self):
        """removed alive = False things from the game"""
         
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for enemys in self.enemy_ships:
            if not enemys.alive:
                self.enemy_ships.remove(enemys)

    # def break_apart(self):

    # def draw_gameover(self):
    #     """once player is dead it desplays death message"""
        
    #     text = "GAME OVER"
    #     start_x = 80
    #     start_y = 250
    #     arcade.draw_text(text, start_x=start_x, start_y=start_y, font_size=100,color=arcade.color.RED)

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
                bullet = Bullet.Bullet (self.ship.center.x, self.ship.center.y + 5, self.ship.velocity.dx, self.ship.velocity.dy)
                self.bullets.append(bullet)
                arcade.play_sound(self.shoot_sound)


    def on_key_release(self, key: int, modifiers: int):
        """
            Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# c = constants


# window = Game(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
# arcade.run()