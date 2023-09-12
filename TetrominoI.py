
from main.Tetromino import Tetromino
from enum import Enum

class rotateState(Enum):
    State1 = 1 #starting state
    State2 = 2 #rotate left or up
    State3 = 3
    State4 = 4


class TetrominoI(Tetromino):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().change_color(0, 0, 1)
        self.TetrominoLocation.append([0, 4])
        self.TetrominoLocation.append([1, 4])
        self.TetrominoLocation.append([2, 4])
        self.TetrominoLocation.append([3, 4])
        self.RotationPosition = rotateState.State1

    def rotate_right(self):
        "create 4 different positions that the blocks can be in"

        if self.RotationPosition == rotateState.State1:
            val = []
            val.append((self.TetrominoLocation[1])[0]) # self.TetrominoLocation[1] gets the position 1 in the list of 4 blocks in the tetromino The [0] and [1] makes a deep copy of the x,y location of the blocks row and columns
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 2
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State2

        elif self.RotationPosition == rotateState.State2:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 2
            val[1] = val[1]
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State3


        elif self.RotationPosition == rotateState.State3:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 2
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State4

        elif self.RotationPosition == rotateState.State4:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 2
            val[1] = val[1]
            self.TetrominoLocation[3] = val

            self.RotationPosition = rotateState.State1


    def rotate_left(self):

        if self.RotationPosition == rotateState.State1:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 2
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State4

        elif self.RotationPosition == rotateState.State4:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 2
            val[1] = val[1]
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State3

        elif self.RotationPosition == rotateState.State3:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0]
            val[1] = val[1] - 2
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State2

        elif self.RotationPosition == rotateState.State2:

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val

            val = []
            val.append((self.TetrominoLocation[1])[0])
            val.append((self.TetrominoLocation[1])[1])
            val[0] = val[0] + 2
            val[1] = val[1]
            self.TetrominoLocation[3] = val
            self.RotationPosition = rotateState.State1

