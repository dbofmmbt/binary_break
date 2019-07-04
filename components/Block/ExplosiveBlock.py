from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball


class ExplosiveBlock(Block):
    def __init__(self):
        img_url = "images/block/red.png"
        super().__init__(img_url)

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        ball.handle_collision(self)
        matrix.handle_explosion(self)

    def update_score(self, blocks_exploded: int):
        self.score_value += blocks_exploded * 10