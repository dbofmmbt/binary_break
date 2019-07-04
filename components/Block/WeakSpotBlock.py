from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball


class WeakSpotBlock(Block):
    def __init__(self):
        img_url = "images/block/yellow.png"
        super().__init__(img_url)

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        pass
