import binary_break.globals as globals


class Counter:
    def __init__(self, default_duration=3):
        self.active = False
        self.default_duration = default_duration
        self.current_duration = 0

    def update_logic(self):
        if self.active:
            self.current_duration -= globals.delta_time
            if self.current_duration <= 0:
                self.active = False

    def start(self):
        self.active = True
        self.current_duration = self.default_duration
