from PPlay.sprite import Sprite
import binary_break.globals as globals


class Pad(Sprite):
    def __init__(self, imageUrl):
        super().__init__(imageUrl)
        self.window = globals.window
        self.set_position(self.window.width/2 - self.width/2, self.window.height * 0.85)

    def render(self):
        self.draw()
