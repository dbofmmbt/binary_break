from binary_break.components.button import Button
import binary_break.globals as globals
from PPlay.gameimage import GameImage


class Menu:
    def __init__(self):
        self.window = globals.window
        self.window.set_title("Invaders Menu")

        self.play = Button("images/menu/play.png")
        self.quit = Button("images/menu/quit.png")

        self.put_button_on_position(self.play, 0.33)
        self.put_button_on_position(self.quit, 0.53)

    def render(self):
        self.update_logic()
        self.window.set_background_color((33, 33, 33))

        self.play.render()
        self.quit.render()

    def update_logic(self):
        if self.play.clicked():
            from binary_break.screens.game import Game
            globals.currentContainer = Game()
        elif self.quit.clicked():
            self.window.close()

    def put_button_on_position(self, button, height_percentage):
        half_width = self.window.width / 2
        button.set_position(half_width - button.width/2, self.window.height * height_percentage)
