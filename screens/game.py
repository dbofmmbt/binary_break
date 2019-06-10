import binary_break.globals as globals
from binary_break.components.pad import Pad
from binary_break.components.ball import Ball
from PPlay.gameimage import GameImage
from binary_break.components.BlockMatrix import BlockMatrix


class Game:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Binary Break!")
        self.background = GameImage("images/background.jpg")

        self.pad = Pad()
        self.ball = Ball()
        self.blocks = BlockMatrix()
        for i in range(10):
            self.blocks.add_line(19)

        self.ball.set_position(self.pad.x + self.pad.width / 2 - self.ball.width / 2, self.pad.y - self.ball.height)
        self.game_started = False

        self.game_over = False
        self.block_rain_duration = 1.5
        self.block_rain_speed = 0.03
        self.block_rain_reload = self.block_rain_speed

    def update_logic(self):
        if not self.game_started:
            self.detect_game_start()
        if self.ball.collided(self.pad):
            self.ball.collision_change("VERTICAL")

        if self.ball.collided_with_bottom():
            self.game_over = True

        if self.window.get_keyboard().key_pressed("ESC"):
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

        for line in self.blocks:
            for block in line:
                if self.ball.verify_collision(block):
                    self.blocks.remove_element(block)

    def render(self):
        self.update_logic()
        self.background.draw()
        if self.game_started:
            self.pad.render()
            self.ball.render()
        else:
            self.pad.draw()
            self.ball.update()
            self.ball.draw()

        if self.game_over and self.block_rain_duration > 0:
            self.block_rain_duration -= globals.delta_time
            self.run_block_rain()

        for line in self.blocks:
            for block in line:
                block.render()

    def detect_game_start(self):
        if self.window.get_keyboard().key_pressed("SPACE"):
            self.game_started = True

    def run_block_rain(self):
        self.block_rain_reload -= globals.delta_time
        if self.block_rain_reload < 0:
            self.blocks.add_line(19)
            self.block_rain_reload = self.block_rain_speed
