from binary_break.components.Block.Block import Block

import random


class BlockMatrix(list):
    def __init__(self):
        from binary_break import CommonBlock, DelayedBlock, ExplosiveBlock, ResistantBlock, SpecialBlock, WeakSpotBlock
        self.width = 600
        self.kinds = (
            CommonBlock, DelayedBlock, ExplosiveBlock, ResistantBlock, SpecialBlock, WeakSpotBlock
        )
        self.x = 0
        self.y = 0

    def update_logic(self):
        pass

    def add_line(self, quantity):
        line = [self.kinds[random.randint(0, 4)]() for _ in range(quantity)]
        x = self.x
        for el in line:
            el.set_position(x, 0)
            x += el.width
        self.move_lines_down()
        self.insert(0, line)

    def move_lines_down(self):
        for line in self:
            for element in line:
                element.move_y(element.height)

    def for_each_element(self, callback):
        for line in self:
            for element in line:
                callback(element)

    def collided_with(self, sprite):
        for line in self:
            for element in line:
                if element.collided_with(sprite):
                    return True
        return False

    def remove_element(self, el):
        for line in self:
            if el in line:
                line.remove(el)
                return
