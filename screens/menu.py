from binary_break.components.button import Button
import binary_break.globals as globals
from PPlay.gameimage import GameImage


class Menu:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Binary Break Menu")

        self.play = Button("images/menu/play.png")
        self.rank = Button("images/menu/rank.png")
        self.quit = Button("images/menu/quit.png")

        self.put_button_on_position(self.play, 0.23)
        self.put_button_on_position(self.rank, 0.43)
        self.put_button_on_position(self.quit, 0.63)

    def render(self):
        self.update_logic()
        self.window.set_background_color((33, 33, 33))

        self.play.render()
        self.rank.render()
        self.quit.render()

    def update_logic(self):
        if self.play.clicked():
            from binary_break.screens.game import Game
            globals.currentContainer = Game()
        elif self.rank.clicked():
            from binary_break.screens.rank import Rank
            globals.currentContainer = Rank()
        elif self.quit.clicked():
            self.window.close()

    def put_button_on_position(self, button, height_percentage):
        half_width = self.window.width / 2
        button.set_position(half_width - button.width / 2, self.window.height * height_percentage)
