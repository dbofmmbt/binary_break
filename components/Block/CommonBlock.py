from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball


class CommonBlock(Block):
    def __init__(self):
        img_url = "images/block/gray.png"
        super().__init__(img_url)

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        matrix.remove_element(self)
        ball.handle_collision(self) if ball else None
