import binary_break.globals as globals
from binary_break.components.pad import Pad


class Game:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Binary Break!")
        self.window.set_background_color(globals.backgroundColor)

        self.pad = Pad("images/pad.png")

    def update(self):
        pass

    def render(self):
        self.pad.render()
