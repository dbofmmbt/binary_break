from PPlay.sprite import Sprite
import binary_break.globals as globals


class Block(Sprite):
    def __init__(self, image_url, quantity_sprites=1):
        super().__init__(image_url, quantity_sprites)
        self.score_value = 10

    def render(self):
        self.update_logic()
        self.draw()

    def update_logic(self):
        pass

    def collided_with(self, obj):
        return self.collided(obj)

    def handle_collision(self, ball, matrix):
        pass
