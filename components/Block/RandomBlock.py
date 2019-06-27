from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball


class RandomBlock(Block):
    def __init__(self):
        img_url = "images/block/blue.jpg"
        super().__init__(img_url)

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        matrix.remove_element(self)
        ball.handle_collision(self)
