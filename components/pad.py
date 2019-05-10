from PPlay.sprite import Sprite


class Pad(Sprite):
    def __init__(self, window, imageUrl):
        super().__init__(imageUrl)
        self.set_position(window.width/2 - self.width/2, window.height * 0.85)

    def render(self):
        self.draw()
