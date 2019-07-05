import random

from PPlay.sprite import Sprite
import binary_break.globals as globals
from binary_break.screens.game import Game

items = [
    ("unstoppable", "images/special/item02.png", 1),
    ("game_over", "images/special/morte-subita.png", 1),
    ("coin_boost", "images/special/boostpoints.png", 4)
]


class Item(Sprite):
    def __init__(self, initial_position):
        item = items[random.randrange(len(items))]
        super().__init__(item[1], item[2])
        self.set_total_duration(500)
        self.item = item
        self.base_speed = 300
        self.score = 0
        self.x = initial_position[0]
        self.y = initial_position[1]

    def update_logic(self):
        self.update()
        self.move_down()

    def render(self):
        self.update_logic()
        self.draw()

    def handle_effect(self, game: Game):
        game.items.remove(self)

        if self.item[0] == "game_over":
            game.lives -= 1
            return
        elif self.item[0] == "coin_boost":
            game.update_score(500)
            return
        elif self.item[0] == "unstoppable":
            game.ball.speed_y += 50

        game.effects[self.item[0]].start()

    def move_down(self):
        self.move_y(self.base_speed * globals.delta_time)
