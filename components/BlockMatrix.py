import random


class BlockMatrix(list):
    def __init__(self, quantity_blocks):
        from binary_break import CommonBlock, DelayedBlock, ExplosiveBlock, ResistantBlock, SpecialBlock, WeakSpotBlock
        self.width = 600
        self.kinds = (
            CommonBlock, DelayedBlock, ExplosiveBlock, ResistantBlock, SpecialBlock, WeakSpotBlock
        )
        self.x = 0
        self.y = 0
        self.quantity_blocks = 0
        self.quantity_blocks_line = quantity_blocks

    def update_logic(self):
        blocks_per_line = self.quantity_blocks // len(self)
        if blocks_per_line < 15 and random.random() > 0.999:
            self.add_random_block()

    def add_line(self):
        line = [self.kinds[random.randint(0, 4)]() for _ in range(self.quantity_blocks_line)]
        x = self.x
        for el in line:
            el.set_position(x, 0)
            x += el.width
        self.move_lines_down()
        self.insert(0, line)
        self.quantity_blocks += self.quantity_blocks_line

    def move_lines_down(self):
        for line in self:
            for element in line:
                element.move_y(element.height) if element else None

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
            for i in range(len(line)):
                if line[i] == el:
                    line[i] = None
                    self.quantity_blocks -= 1
                    return

    def handle_explosion(self, explosive_block):
        for i in range(len(self)):
            for j in range(len(self[i])):
                if self[i][j] == explosive_block:
                    quantity_exploded = self.explosion_removal(i, j)
                    explosive_block.update_score(quantity_exploded)
                    return

    def explosion_removal(self, line, column):
        start_column = column - 1 if column > 0 else column
        end_column = column + 1 if column < self.quantity_blocks_line - 1 else column
        start_line = line - 1 if line > 0 else line
        end_line = line + 1 if line < len(self) - 1 else line
        blocks_removed = 0

        for i in range(start_line, end_line + 1):
            for j in range(start_column, end_column + 1):
                blocks_removed += 1
                self[i][j] = None
                self.quantity_blocks -= 1
        return blocks_removed

    def add_random_block(self):
        from binary_break.components.Block.RandomBlock import RandomBlock
        block_added = False
        get_int = random.randrange
        while not block_added:
            i, j = get_int(0, len(self)), get_int(0, self.quantity_blocks_line)
            if self[i][j]:
                continue
            else:
                self[i][j] = RandomBlock()
                width, height = self[i][j].width, self[i][j].height
                self[i][j].set_position(self.x + width * j, height * i)
                self.quantity_blocks += 1
                block_added = True
