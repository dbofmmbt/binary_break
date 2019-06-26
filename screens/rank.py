from binary_break.components.button import Button
import binary_break.globals as globals
from binary_break.screens.menu import Menu
import time


class Rank:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Binary Break Rank")

        self.quit = Button("images/menu/quit.png")
        self.put_button_on_position(self.quit, 0.73)
        score_file = open("data/score.txt", "r+")
        self.scores = []
        for line in score_file:
            name, score = line.split()
            self.scores.append([name, int(score)])
        score_file.close()
        self.scores.sort(key=lambda item: item[1], reverse=True)
        self.scores = self.scores[:5]

    def render(self):
        self.update_logic()
        self.window.set_background_color((33, 33, 33))

        self.show_score()
        self.quit.render()

    def update_logic(self):
        if self.quit.clicked():
            globals.currentContainer = Menu()

    def put_button_on_position(self, button, height_percentage):
        half_width = self.window.width / 2
        button.set_position(half_width - button.width / 2, self.window.height * height_percentage)

    def show_score(self):
        y = 100
        name_x = self.window.width / 2 - 200
        score_x = name_x + 250
        self.window.draw_text("Nome", name_x, y, 32, (255, 255, 255), bold=True, font_name="Monospace")
        self.window.draw_text("Pontuação", score_x, y, 32, (255, 255, 255), bold=True, font_name="Monospace")
        for score in self.scores:
            y += 40
            self.window.draw_text("{}".format(score[0]), name_x, y, 32, (255, 255, 255), font_name="Monospace")
            self.window.draw_text("{}".format(score[1]), score_x, y, 32, (255, 255, 255), font_name="Monospace")
