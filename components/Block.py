from PPlay.sprite import Sprite
import binary_break.globals as globals


class Block(Sprite):
    def __init__(self, color):
        image_url = f"images/block/{color}.jpg"
        super().__init__(image_url)

    def render(self):
        self.update_logic()
        self.draw()

    def update_logic(self):
        pass

    def collided_with(self, obj):
        return self.collided(obj)
