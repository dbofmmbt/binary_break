from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.Item.Item import Item
from binary_break.components.ball import Ball


class SpecialBlock(Block):
    add_special_item = None

    def __init__(self):
        img_url = "images/block/purple.png"
        super().__init__(img_url)

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        ball.handle_collision(self) if ball else None
        matrix.remove_element(self) if matrix else None
        SpecialBlock.add_special_item(Item((self.x, self.y)))
