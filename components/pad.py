from PPlay.sprite import Sprite
import binary_break.globals as globals


class Pad(Sprite):
    def __init__(self):
        super().__init__("images/pad.png")
        self.window = globals.window
        self.keyboard = self.window.get_keyboard()
        self.set_position(self.window.width/2 - self.width/2, self.window.height * 0.85)
        self.speed = 400

    def render(self):
        self.updateLogic()
        self.draw()

    def updateLogic(self):
        self.checkMovement()
        self.mustBeInDisplay()

    def mustBeInDisplay(self):
        if self.x < 0:
            self.set_position(0, self.y)
        elif self.x+self.width > self.window.width:
            self.set_position(self.window.width-self.width, self.y)

    def checkMovement(self):
        if self.keyboard.key_pressed("RIGHT"):
            self.move_x(self.speed * globals.delta_time)
        elif self.keyboard.key_pressed("LEFT"):
            self.move_x(-self.speed * globals.delta_time)
