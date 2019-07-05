import random

from PPlay.sprite import Sprite
import binary_break.globals as globals
from binary_break.screens.game import Game

items = [("unstoppable", "images/special/item02.png", 1), ("game_over", "images/special/morte-subita.png", 1)]


class Item(Sprite):
    def __init__(self, initial_position):
        item = random.choice(items)
        super().__init__(item[1], item[2])
        self.item = item
        self.base_speed = 300
        self.score = 0
        self.x = initial_position[0]
        self.y = initial_position[1]

    def update_logic(self):
        self.move_down()

    def render(self):
        self.update_logic()
        self.draw()

    def handle_effect(self, game: Game):
        game.effects[self.item[0]].start()
        game.items.remove(self)

    def move_down(self):
        self.move_y(self.base_speed * globals.delta_time)
