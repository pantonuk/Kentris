from main.Tetromino import Tetromino
from enum import Enum

class rotateState(Enum):
    State1 = 1 #starting state
    State2 = 2 #rotate left or up
    State3 = 3
    State4 = 4


class TetrominoO(Tetromino):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().change_color(.5, .5, .5)

        self.TetrominoLocation.append([0, 4])
        self.TetrominoLocation.append([0, 5])
        self.TetrominoLocation.append([1, 4])
        self.TetrominoLocation.append([1, 5])
        self.RotationPosition = rotateState.State1

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

