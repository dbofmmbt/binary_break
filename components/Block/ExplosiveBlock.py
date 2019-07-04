from binary_break.components.Block.Block import Block
from binary_break.components.ball import Ball


class ExplosiveBlock(Block):
    def __init__(self):
        img_url = "images/block/red.png"
        super().__init__(img_url)
        self.should_explode = True

    def handle_collision(self, ball: Ball, matrix):
        ball.handle_collision(self) if ball else None
        matrix.handle_explosion(self) if self.should_explode else None
        matrix.remove_element(self)

