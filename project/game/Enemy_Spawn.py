import arcade
import random


class Enemy_Spawn:

    def __init__(self, create_ships):
        self.create_ships = create_ships()
        self.spawn_rate = random.randint(0, 3)

    def spawn_rate(self, delta_time):

        for enemy in self.enemy_ships:
            arcade.schedule(self.create_ships(), self.spawn_rate)

