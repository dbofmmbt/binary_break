from binary_break.components.Block import Block
import random
import binary_break.globals as globals


class BlockMatrix(list):
    def __init__(self):
        self.width = 600
        self.colors = (
            "red", "pink", "orange", "blue", "green"
        )

    def update_logic(self):
        pass

    def add_line(self, quantity):
        line = [Block(self.colors[random.randint(0, 4)]) for i in range(quantity)]
        x = 0
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
