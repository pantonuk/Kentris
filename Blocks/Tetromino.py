
class Tetromino():

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.TetrominoLocation = []
        self.stopped = False
        self.red = 0
        self.green = 0
        self.blue = 0

    def change_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass
