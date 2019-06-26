from PPlay.window import Window
import binary_break.globals as globals
from binary_break.screens.menu import Menu

window = Window(800, 700)
keyboard = window.get_keyboard()

globals.window = window
globals.difficulty = 1
globals.backgroundColor = (10, 11, 56)
globals.game_speed = 1
globals.currentContainer = Menu()

while True:
    globals.delta_time = window.delta_time()
    globals.currentContainer.render()
    window.update()
