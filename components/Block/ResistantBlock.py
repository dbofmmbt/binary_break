from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball


class ResistantBlock(Block):
    def __init__(self):
        img_url = "images/block/green.png"
        super().__init__(img_url, 3)
        self.set_total_duration(0)
        self.hits_to_explode = 3
        self.score_value = 20

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        self.hits_to_explode -= 1
        self.update()
        ball.handle_collision(self)

        if self.hits_to_explode <= 0:
            matrix.remove_element(self)
