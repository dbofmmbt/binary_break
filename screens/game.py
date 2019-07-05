import binary_break.globals as globals
from binary_break.components.Counter import Counter
from binary_break.components.pad import Pad
from binary_break.components.ball import Ball
from PPlay.gameimage import GameImage
from binary_break.components.BlockMatrix import BlockMatrix


class Game:
    def __init__(self):
        from binary_break import SpecialBlock
        SpecialBlock.add_special_item = self.add_special_item

        self.window = globals.window
        self.window.set_title("Binary Break!")
        self.background = GameImage("images/background.jpg")
        self.lateral_bar = GameImage("images/back2.jpg")

        self.game_width = 600
        self.blocks = BlockMatrix(10)
        x_start_point = self.window.width - self.game_width
        self.pad = Pad(x_start_point)
        self.ball = Ball()
        self.ball.min_x = self.blocks.x = x_start_point
        self.put_ball_over_pad()

        for i in range(5):
            self.blocks.add_line()

        self.game_started = False
        self.score = 0
        self.score_increment_rate = 0.1

        self.game_over = False
        self.block_rain_counter = Counter(1.5)
        self.rain_line_counter = Counter(0.03)

        self.items = []
        durable_effects = ("unstoppable", "game_over")

        self.effects = {effect: Counter() for effect in durable_effects}

    def update_counters(self):
        self.block_rain_counter.update_logic()
        self.rain_line_counter.update_logic()
        for counter in self.effects.values():
            counter.update_logic()

    def update_effects(self):
        self.ball.unstoppable = self.effects["unstoppable"].active
        self.game_over = self.game_over or self.effects["game_over"].active

    def update_score(self, score):
        if not self.game_over:
            self.score += score

    def update_logic(self):
        self.update_counters()
        self.update_effects()

        if not self.game_started:
            self.detect_game_start()
            return
        if self.ball.collided(self.pad):
            self.ball.handle_collision(self.pad)

        if self.ball.collided_with_bottom() and not self.game_over:
            self.game_over = True
            self.block_rain_counter.start()

        if self.window.get_keyboard().key_pressed("ESC"):
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

        self.blocks.update_logic()

        for line in self.blocks:
            for block in line:
                if block and self.ball.collided(block):
                    block.handle_collision(self.ball, self.blocks)
                    self.update_score(block.score_value)

        for item in self.items:
            if item.collided(self.pad):
                item.handle_effect(self)

        self.score_increment_rate -= globals.delta_time
        if self.score_increment_rate < 0 and not self.game_over:
            self.score_increment_rate = 0.1
            self.update_score(1)

        if self.block_rain_counter.active:
            self.run_block_rain()

        if self.game_over and not self.block_rain_counter.active:
            self.register_score()
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

    def render(self):
        self.update_logic()
        self.window.set_background_color(globals.backgroundColor)
        self.background.draw()
        self.lateral_bar.draw()

        self.pad.render()

        if self.game_started:
            self.ball.render()
        else:
            self.put_ball_over_pad()
            self.ball.update()
            self.ball.draw()

        for line in self.blocks:
            for block in line:
                block.render() if block else None

        if not self.game_over:
            for item in self.items:
                item.render()

        self.show_score()

    def detect_game_start(self):
        if self.window.get_keyboard().key_pressed("SPACE"):
            self.game_started = True

    def run_block_rain(self):
        if not self.rain_line_counter.active:
            self.blocks.add_line()
            self.rain_line_counter.start()

    def show_score(self):
        text = "SCORE:{}".format(self.score)
        # text_space = len(text) * 14
        self.window.draw_text(
            text=text,
            x=50,
            y=40,
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

    def add_special_item(self, item):
        if not self.game_over:
            self.items.append(item)

    def put_ball_over_pad(self):
        self.ball.set_position(self.pad.x + self.pad.width / 2 - self.ball.width / 2, self.pad.y - self.ball.height)
