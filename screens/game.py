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
        self.game_started = False

    def update_logic(self):
        if not self.game_started:
            self.detect_game_start()

    def render(self):
        self.window.set_background_color(globals.backgroundColor)
        self.pad.render()
        if self.game_started:
            self.ball.render()
        else:
            self.ball.update()
            self.ball.draw()

    def detect_game_start(self):
        if self.window.get_keyboard().key_pressed("SPACE"):
            self.game_started = True
