from PPlay.window import Window
import binary_break.globals as globals
from binary_break.screens.game import Game

window = Window(700, 700)
keyboard = window.get_keyboard()

globals.window = window
globals.difficulty = 1
globals.backgroundColor = (10, 11, 56)
globals.currentContainer = Game()

while True:
    globals.currentContainer.update()
    globals.currentContainer.render()
    window.update()
