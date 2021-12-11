from arcade.window_commands import schedule, set_background_color
import game.constants as constants
import game.Your_Ship as Your_Ship
import arcade
import random
from game.Enemys import Big_Boat
import game.Bullet as Bullet
import Game_Over
import game.background as background
import arcade.gui



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
        self.song = arcade.sound.load_sound("project/game/sound.mp3")
        self.background = background.Background()

        self.score=0




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

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = constants.SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE)
            

    def update(self, delta_time):
        """Deals with all the updates. things like Movement, Collision, and bullet/ship info"""

        self.check_keys()
        self.check_collisions()
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

        self.create_ships()
    
        
    
    def setup(self):
        pass

    def create_ships(self):
        """builds the Big_Boats"""
        if self.shipcount !=0:
            self.enemy_ship = Big_Boat()
            self.enemy_ships.append(self.enemy_ship)
            self.shipcount -=1

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
                        self.score += 1
                        self.shipcount += 2
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
                        # arcade.sound.stop_sound()

        self.cleanup_zombies()

    def cleanup_zombies(self):
        """removed alive = False things from the game"""
         
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for enemys in self.enemy_ships:
            if not enemys.alive:
                self.enemy_ships.remove(enemys)



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
    


