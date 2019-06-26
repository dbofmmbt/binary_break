from PPlay.sprite import Sprite
import binary_break.globals as globals


class Pad(Sprite):
    def __init__(self, min_x):
        super().__init__("images/pad.png")
        self.window = globals.window
        self.keyboard = self.window.get_keyboard()
        self.set_position((self.window.width + min_x - self.width) / 2, self.window.height * 0.85)
        self.speed = 400
        self.min_x = min_x

    def render(self):
        self.update_logic()
        self.draw()

    def update_logic(self):
        self.check_movement()
        self.must_be_in_display()

    def must_be_in_display(self):
        if self.x < self.min_x:
            self.set_position(self.min_x, self.y)
        elif self.x + self.width > self.window.width:
            self.set_position(self.window.width - self.width, self.y)

    def check_movement(self):
        if self.keyboard.key_pressed("RIGHT"):
            self.move_x(self.speed * globals.delta_time)
        elif self.keyboard.key_pressed("LEFT"):
            self.move_x(-self.speed * globals.delta_time)
