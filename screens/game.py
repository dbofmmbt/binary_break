import binary_break.globals as globals
from binary_break.components.pad import Pad

class Game:
    def __init__(self, window):
        self.window = window
        window.set_title("Binary Break!")
        window.set_background_color(globals.backgroundColor)

        self.pad = Pad(window, "images/pad.png")

    def update(self):
        pass

    def render(self):
        self.pad.render()
