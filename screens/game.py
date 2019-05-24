import binary_break.globals as globals
from binary_break.components.pad import Pad
from binary_break.components.ball import Ball

class Game:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Binary Break!")

        self.pad = Pad()
        self.ball = Ball()
        self.ball.set_position(self.pad.x + self.pad.width/2 - self.ball.width/2, self.pad.y - self.ball.height)

    def update(self):
        pass

    def render(self):
        self.window.set_background_color(globals.backgroundColor)
        self.pad.render()
        self.ball.render()
