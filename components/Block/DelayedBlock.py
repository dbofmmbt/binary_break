from binary_break.components.Block.Block import Block
from binary_break.components.BlockMatrix import BlockMatrix
from binary_break.components.ball import Ball
import binary_break.globals as globals


class DelayedBlock(Block):
    def __init__(self):
        img_url = "images/block/blue.png"
        super().__init__(img_url)
        self.was_hit = False
        self.delay = 3
        self.blink_reload = 0.3
        self.show = True
        self.matrix = None

    def render(self):
        self.update_logic()
        if self.show:
            self.draw()

    def update_logic(self):
        if self.was_hit:
            self.delay -= globals.delta_time
            self.blink_reload -= globals.delta_time
            if self.delay < 0:
                self.matrix.remove_element(self)
            elif self.delay > 0 and self.blink_reload < 0:
                self.blink_reload = 0.3
                self.show = not self.show

    def handle_collision(self, ball: Ball, matrix: BlockMatrix):
        if not self.was_hit:
            self.matrix = matrix
            self.show = False
            self.was_hit = True
        ball.handle_collision(self) if ball else None
