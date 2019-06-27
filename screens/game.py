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
        self.game_width = 600
        x_start_point = self.window.width - self.game_width
        self.pad = Pad(x_start_point)
        self.ball = Ball()
        self.blocks = BlockMatrix(19)
        self.ball.min_x = self.blocks.x = x_start_point
        for i in range(10):
            self.blocks.add_line()

        self.ball.set_position(self.pad.x + self.pad.width / 2 - self.ball.width / 2, self.pad.y - self.ball.height)
        self.game_started = False
        self.score = 0
        self.score_increment_rate = 0.1

        self.game_over = False
        self.block_rain_duration = 1.5
        self.block_rain_speed = 0.03
        self.block_rain_reload = self.block_rain_speed

    def update_logic(self):
        if not self.game_started:
            self.detect_game_start()
            return
        if self.ball.collided(self.pad):
            self.ball.collision_change("VERTICAL")

        if self.ball.collided_with_bottom():
            self.game_over = True

        if self.window.get_keyboard().key_pressed("ESC"):
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

        for line in self.blocks:
            for block in line:
                if block and self.ball.collided(block):
                    block.handle_collision(self.ball, self.blocks)
                    self.score += block.score_value

        self.score_increment_rate -= globals.delta_time
        if self.score_increment_rate < 0 and not self.game_over:
            self.score_increment_rate = 0.1
            self.score += 1

        if self.game_over and self.block_rain_duration <= 0:
            self.register_score()
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

    def render(self):
        self.update_logic()
        self.window.set_background_color(globals.backgroundColor)
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
                block.render() if block else None
        self.show_score()

    def detect_game_start(self):
        if self.window.get_keyboard().key_pressed("SPACE"):
            self.game_started = True

    def run_block_rain(self):
        self.block_rain_reload -= globals.delta_time
        if self.block_rain_reload < 0:
            self.blocks.add_line()
            self.block_rain_reload = self.block_rain_speed

    def show_score(self):
        text = "SCORE: {}".format(self.score)
        # text_space = len(text) * 14
        self.window.draw_text(
            text=text,
            x=20,
            y=20,
            size=24,
            color=(200, 200, 200),
            font_name="Monospace",
            bold=True
        )

    def register_score(self):
        name = input("Por favor, digite seu nome/nickname: ").strip()
        score_file = open("data/score.txt", "a+")
        score_file.write("{} {}\n".format(name, self.score))
        score_file.close()
