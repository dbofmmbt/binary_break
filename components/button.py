from PPlay.animation import *
from PPlay.mouse import *
import binary_break.globals as globals


class Button(Animation):
    def __init__(self, imageUrl):
        super().__init__(imageUrl, 2)
        self.set_total_duration(0)
        self.window = globals.window
        self.mouse = globals.window.get_mouse()
        self.was_mouse_over = False

    def clicked(self):
        mouse_over_button = self.mouseOver()
        mouse_clicked = self.mouse.is_button_pressed(BUTTON_LEFT)
        return mouse_over_button and mouse_clicked

    def mouseOver(self):
        start_point = [self.x, self.y]
        finish_point = [self.x + self.width, self.y + self.height]
        return self.mouse.is_over_area(start_point, finish_point)

    def shouldAnimate(self):
        got_over_button = self.mouseOver() and not self.was_mouse_over
        got_out_button = not self.mouseOver() and self.was_mouse_over
        return got_over_button or got_out_button

    def render(self):
        if self.shouldAnimate():
            self.update()
            self.was_mouse_over = not self.was_mouse_over
        self.draw()
