from PPlay.window import Window
import binary_break.globals as globals
from binary_break.screens.game import Game

window = Window(800, 600)
keyboard = window.get_keyboard()

globals.difficulty = 1
globals.backgroundColor = (10, 11, 56)
globals.currentContainer = Game(window)

while True:
    globals.currentContainer.update()
    globals.currentContainer.render()
    window.update()
