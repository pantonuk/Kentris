from Blocks.Tetromino import Tetromino
from enum import Enum

class rotateState(Enum):
    State1 = 1 #starting state
    State2 = 2 #rotate left or up
    State3 = 3
    State4 = 4


class TetrominoS(Tetromino):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        super().change_color(0, 1, 0)

        self.TetrominoLocation.append([0, 5])
        self.TetrominoLocation.append([0, 6])
        self.TetrominoLocation.append([1, 4])
        self.TetrominoLocation.append([1, 5])
        self.RotationPosition = rotateState.State1

    def rotate_right(self):

        if self.RotationPosition == rotateState.State1:
            val = []
            val.append((self.TetrominoLocation[3])[0])  # self.TetrominoLocation[1] gets the position 1 in the list of 4 blocks in the tetromino The [0] and [1] makes a deep copy of the x,y location of the blocks row and columns
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1] + 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State2

        elif self.RotationPosition == rotateState.State2:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1] - 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State3


        elif self.RotationPosition == rotateState.State3:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1] - 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State4

        elif self.RotationPosition == rotateState.State4:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1] + 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[2] = val

            self.RotationPosition = rotateState.State1

    def rotate_left(self):

        if self.RotationPosition == rotateState.State1:
            val = []
            val.append((self.TetrominoLocation[3])[0])  # self.TetrominoLocation[1] gets the position 1 in the list of 4 blocks in the tetromino The [0] and [1] makes a deep copy of the x,y location of the blocks row and columns
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1] - 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State4

        elif self.RotationPosition == rotateState.State4:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1] - 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State3


        elif self.RotationPosition == rotateState.State3:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] + 1
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] + 1
            val[1] = val[1] + 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[2] = val
            self.RotationPosition = rotateState.State2

        elif self.RotationPosition == rotateState.State2:

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1]
            self.TetrominoLocation[0] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0] - 1
            val[1] = val[1] + 1
            self.TetrominoLocation[1] = val

            val = []
            val.append((self.TetrominoLocation[3])[0])
            val.append((self.TetrominoLocation[3])[1])
            val[0] = val[0]
            val[1] = val[1] - 1
            self.TetrominoLocation[2] = val

            self.RotationPosition = rotateState.State1
