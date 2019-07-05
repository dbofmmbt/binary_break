import binary_break.globals as globals
from binary_break.components.Counter import Counter
from binary_break.components.pad import Pad
from binary_break.components.ball import Ball
from PPlay.gameimage import GameImage
from binary_break.components.BlockMatrix import BlockMatrix
from PPlay.sound import Sound


class Game:
    def __init__(self):
        from binary_break import SpecialBlock
        SpecialBlock.add_special_item = self.add_special_item

        self.window = globals.window
        self.window.set_title("Space Breakout")
        self.background = GameImage("images/background.jpg")
        self.lateral_bar = GameImage("images/back2.jpg")
        self.sound = Sound("sound/gametheme.wav")
        self.sound.loop = True
        quantity_columns = 10
        self.game_width = SpecialBlock().width * quantity_columns
        self.blocks = BlockMatrix(quantity_columns)
        x_start_point = self.window.width - self.game_width
        self.pad = Pad(x_start_point)
        self.ball = Ball()
        self.ball.min_x = self.blocks.x = x_start_point
        self.put_ball_over_pad()

        for i in range(5):
            self.blocks.add_line()

        self.game_started = False
        self.lives = 3
        self.score = 0
        self.score_increment_rate = 0.1

        self.game_over = False
        self.block_rain_counter = Counter(1.5)
        self.rain_line_counter = Counter(0.03)

        self.items = []
        durable_effects = ("unstoppable", )

        self.effects = {effect: Counter() for effect in durable_effects}

    def update_counters(self):
        self.block_rain_counter.update_logic()
        self.rain_line_counter.update_logic()
        for counter in self.effects.values():
            counter.update_logic()

    def update_effects(self):
        self.ball.unstoppable = self.effects["unstoppable"].active

    def update_score(self, score):
        if not self.game_over:
            self.score += score

    def update_logic(self):
        self.update_counters()
        self.update_effects()
        if not self.game_started and self.lives > 0:
            self.detect_game_start()
            return
        if self.ball.collided(self.pad):
            self.ball.handle_collision(self.pad)

        if self.ball.collided_with_bottom():
            self.lives -= 1
            self.ball.collision_change("VERTICAL")
            self.game_started = False

        if self.lives <= 0 and not self.game_over:
            self.game_over = True
            self.block_rain_counter.start()

        if self.window.get_keyboard().key_pressed("ESC"):
            from binary_break.screens.menu import Menu
            globals.currentContainer = Menu()

        self.blocks.update_logic()

        if self.block_rain_counter.active:
            self.run_block_rain()

        if self.game_over:
            if not self.block_rain_counter.active:
                self.register_score()
                from binary_break.screens.menu import Menu
                globals.currentContainer = Menu()
            return

        for line in self.blocks:
            for block in line:
                if block and self.ball.collided(block):
                    block.handle_collision(self.ball, self.blocks)
                    self.update_score(block.score_value)

        for item in self.items:
            if item.collided(self.pad):
                item.handle_effect(self)

        self.score_increment_rate -= globals.delta_time
        if self.score_increment_rate < 0:
            self.score_increment_rate = 0.1
            self.update_score(1)

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
            self.ball.draw()

        for line in self.blocks:
            for block in line:
                block.render() if block else None

        if not self.game_over:
            for item in self.items:
                item.render()

        self.show_score()
        self.show_lives()
        self.sound.set_volume(20)
        self.sound.play()
        self.sound.set_repeat(True)

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
            x=45,
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

    def show_lives(self):
        life = GameImage("images/life.png")
        life.set_position(78, 170)
        life.draw()

        text = "LIFE:{}".format(self.lives)
        # text_space = len(text) * 14
        self.window.draw_text(
            text=text,
            x=60,
            y=245,
            size=24,
            color=(200, 200, 200),
            font_name="Monospace",
            bold=True
        )
