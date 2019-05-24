from PPlay.sprite import Sprite
import binary_break.globals as globals
import random


class Ball(Sprite):
    def __init__(self):
        super().__init__("images/ball.png", 8)
        self.set_total_duration(1000)
        self.window = globals.window
        self.set_position(self.window.width/2 - self.width/2, self.window.height * 0.85)
        self.speed_x = 300 * globals.game_speed
        self.speed_y = -300 * globals.game_speed

    def render(self):
        self.update_logic()
        self.draw()
        self.update()

    def update_logic(self):
        self.move()
        self.must_be_inside_window()

    def move(self):
        self.move_x(self.speed_x * globals.delta_time)
        self.move_y(self.speed_y * globals.delta_time)

    def must_be_inside_window(self):
        if self.x < 0:
            self.set_position(0, self.y)
            self.collision_change("LATERAL")
        elif self.x+self.width > self.window.width:
            self.set_position(self.window.width-self.width, self.y)
            self.collision_change("LATERAL")
        elif self.y < 0:
            self.set_position(self.x, 0)
            self.collision_change("VERTICAL")

    def collision_change(self, kind):
        if kind == "VERTICAL":
            self.speed_x *= 1 + random.uniform(-0.1, 0.1)
            self.speed_y *= - 1 - random.uniform(-0.1, 0.1)
        elif kind == "LATERAL":
            self.speed_x *= -1 - (random.uniform(-0.1, 0.1))
            self.speed_y *= 1 + random.uniform(-0.1, 0.1)

    def collided_with_bottom(self):
        return self.y + self.height > self.window.height
