from PPlay.sprite import Sprite
import binary_break.globals as globals


class Ball(Sprite):
    def __init__(self):
        super().__init__("images/ball.png", 8)
        self.set_total_duration(1000)
        self.window = globals.window
        self.set_position(self.window.width/2 - self.width/2, self.window.height * 0.85)

    def render(self):
        self.draw()
        self.update()
