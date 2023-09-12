from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

from team01.main.Block import Block
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from kivy.properties import *
from team01.main.Tetromino import Tetromino
from team01.main.TetrominoI import TetrominoI
from team01.main.TetrominoO import TetrominoO
from team01.main.TetrominoT import TetrominoT
from team01.main.TetrominoS import TetrominoS
from team01.main.TetrominoZ import TetrominoZ
from team01.main.TetrominoJ import TetrominoJ
from team01.main.TetrominoL import TetrominoL

#from team01.TetrominoI import tetrominoI
from kivy.core.window import Window

import random



# This is the root of the tetris application and links to the kv file
# it creates the root window into which things are placed. The tetris
# class contains the init functions that create the various UI elements



class TetrisWindow(App):
    pass


# GridLayout that holds the gameboard grid side of the screen
class TetrisGameBoard(GridLayout):
    GameBoardArray = [[0 for i in range(10)] for j in range(20)]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(20):
            for j in range(10):
                block = Block()
                self.GameBoardArray[i][j] = block
                self.add_widget(block)

    def DisplayTetromino(self, tetromino: Tetromino):
        tetroBlock = tetromino.TetrominoLocation

        for i in tetroBlock:
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(tetromino.red, tetromino.green, tetromino.blue)

    def fall_tetromino(self, tetromino: Tetromino):
        tetroBlock = tetromino.TetrominoLocation

        for i in tetroBlock:
            if (i[0] + 1 > 19):
                tetromino.stopped = True
                return

        for i in tetroBlock:
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(0, 0, 0)

        for i in tetroBlock:
            i[0] = i[0] + 1
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(tetromino.red, tetromino.green, tetromino.blue)
        return True
    def break_line(self, x: int):
        for i in range(x + 1):
            for j in range(10):
                block = self.GameBoardArray[i][j]
                block.change_color(0, 0, 0)

    def move_left_tetromino(self, tetromino: Tetromino):
        tetroBlock = tetromino.TetrominoLocation

        for i in tetroBlock:
            if (i[1] <= 0):
                return
            if (i[1] <= 0 and i[1] - 1 == 0):
                tetromino.stopped = True
                return

        for i in tetroBlock:
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(0, 0, 0)

        for i in tetroBlock:
            i[1] = i[1] - 1
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(tetromino.red, tetromino.green, tetromino.blue)

    def move_right_tetromino(self, tetromino: Tetromino):
        tetroBlock = tetromino.TetrominoLocation

        for i in tetroBlock:
            if (i[1] + 1 > 9):
                return
            if (i[1] + 1 > 9 and i[1] - 1 == 0):
                tetromino.stopped = True
                return

        for i in tetroBlock:
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(0, 0, 0)

        for i in tetroBlock:
            i[1] = i[1] + 1
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(tetromino.red, tetromino.green, tetromino.blue)

    def blank_tetromino(self, tetromino: Tetromino):
        tetroBlock = tetromino.TetrominoLocation
        for i in tetroBlock:
            block = self.GameBoardArray[i[0]][i[1]]
            block.change_color(0, 0, 0)

class KentrisMenu(Screen):
    pass


class HelpMenu(Screen):
    pass

class GameBoardPanel(Widget):
    red = NumericProperty(0)
    green = NumericProperty(0)
    blue = NumericProperty(0)

    def change_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


    def display_next_tetromino(self):
        pass

class RestartButton(Button):

    def __init__(self, **kwargs):
        super(RestartButton, self).__init__(**kwargs)
        self.text = "Restart Game"

    def OnPress(self, tetris_board):
        self.LiveTetromino = TetrominoO()
        self.NextTetromino = None
        self.game_over = False

        for i in range(20):
            for j in range(10):
                tetris_board.GameBoardArray[i][j].change_color(0,0,0)
        self.tetrominos = []
        self.clock = None

class Score(Label):
    score = 0
    def __init__(self, **kwargs):
        super(Score, self).__init__(**kwargs)

        self.text = "Score : " + str(self.score)

        self.color = (1, 1, 1, 1)

    def calculate_score(self, deleted_rows):
        if deleted_rows == 1:
            self.score += 40
            self.text = "Score : " + str(self.score)
        elif deleted_rows == 2:
            self.score += 100
            self.text = "Score : " + str(self.score)
        elif deleted_rows == 3:
            self.score += 300
            self.text = "Score : " + str(self.score)
        elif deleted_rows == 4:
            self.score += 1200
            self.text = "Score : " + str(self.score)

    def add_score(self, new_score):
        if new_score == 0:
            self.score = 0
        else:
            self.score = self.score + new_score
            self.text = "Score : " + str(self.score)

    def return_score(self):
        return self.score


class NewGrayBox(BoxLayout):
    def __init__(self, **kwargs):
        super(NewGrayBox, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.6,.6,.6)
            self.rect = Rectangle(size = self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class NextBlock(BoxLayout):
    def __init__(self, **kwargs):
        super(NextBlock, self).__init__(**kwargs)


        with self.canvas.before:
            Color(0,0,0)
            self.rect = Rectangle(size = self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class GameBoard(Screen):  # TODO REFACTOR TO NEW NAME TO PLAY OR SOMETHING TO MAKE MORE SENSE
    ScoreLabel = None
    tetris_board = None
    split_screen = None
    game_board_pannel = None
    tetrominos = []
    LiveTetromino = None
    game_over = False
    clock = None
    score = 0
    deleted_rows = 0
    LeaderboardScores = None
    _on_key_down = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.RestartButton = RestartButton()
        self.container = NewGrayBox(orientation='vertical')
        self.Next_Piece = NextBlock(orientation = 'vertical')
        self._keyboard = Window.request_keyboard(self.on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down)
        self.split_screen = GridLayout(cols=2, rows=1)
        self.second_split_screen = GridLayout(cols=1, rows=2)
        self.ScoreLabel = Score()
        self.New_Box = NewGrayBox(orientation='vertical')
        self.game_board_pannel = GameBoardPanel()
        self.game_board_pannel.change_color(.7, .7, .7)
        self.tetris_board = TetrisGameBoard()
        self.split_screen.add_widget(self.tetris_board)
        self.split_screen.add_widget(self.second_split_screen)
        self.second_split_screen.add_widget(self.Next_Piece)
        self.second_split_screen.add_widget(self.container)
        self.container.add_widget(self.ScoreLabel)
        self.container.add_widget(self.New_Box)
        self.New_Box.add_widget(self.RestartButton)
        self.Leaderboard = []
        self.LeaderboardNames = []

        self.add_widget(self.split_screen)
        self.LiveTetromino = TetrominoO()
        self.NextTetromino = None
        self.tetris_board.DisplayTetromino(self.LiveTetromino)



    def set_clock(self, clock):
        self.clock = clock


    def break_line(self):
        i = 19
        # for each row check if all columns have block by iterating tetrimno list
        while i >= 0:
            columns = []
            # Iterate list of tetrominos
            for j in self.tetrominos:
                # Iterate location to check if on same line
                for k in j.TetrominoLocation:
                    if i == k[0]:
                        columns.append(k[1])
            # if all ten columns are full
            if len(columns) == 10:
                self.score += 10
                # reset the line to black
                self.tetris_board.break_line(i)
                self.deleted_rows += 1
                print(self.deleted_rows)
                # iterate all tetrominos to identify all blocks in the column
                for j in self.tetrominos:
                    remove = []
                    # Identify the blocks to remove
                    for k in range(len(j.TetrominoLocation)):
                        if (j.TetrominoLocation[k])[0] == i:
                            remove.append(k)
                    # remove the blocks from the tetromino
                    for k in reversed(remove):
                        j.TetrominoLocation.pop(k)

                # Fall all other blocks down and redisplay all blocks
                for j in self.tetrominos:
                    for k in j.TetrominoLocation:
                        if i > k[0]:
                            k[0] = k[0] + 1
                    self.tetris_board.DisplayTetromino(j)
            else:
                i = i - 1

    def next_piece_image(self, num, image):

        self.Next_Piece.clear_widgets()

        if (num == 1):
            self.Next_Piece.add_widget(image)
        elif (num == 2):
            self.Next_Piece.add_widget(image)
        elif (num == 3):
            self.Next_Piece.add_widget(image)
        elif (num == 4):
            self.Next_Piece.add_widget(image)
        elif (num == 5):
            self.Next_Piece.add_widget(image)
        elif (num == 6):
            self.Next_Piece.add_widget(image)
        elif (num == 7):
            self.Next_Piece.add_widget(image)

    def Update(self, time):

        self.RestartButton.bind(on_press = lambda x:RestartButton.OnPress(self, self.tetris_board))

        if self.NextTetromino == None:
            self.NextTetromino = random.randint(1, 7)
            self.ScoreLabel.add_score(0)
            self.game_over = False
            self.clock = Clock.schedule_interval(self.Update, 20)

        self.break_line()
        self.calculate_down_collisions()
        self.calculate_game_over()
        self.createNextTetromino(self.NextTetromino)
        self.tetris_board.DisplayTetromino(self.LiveTetromino)
        self.ScoreLabel.calculate_score(self.deleted_rows)
        self.deleted_rows = 0

        if self.game_over:
            for j in self.tetrominos:
                self.tetris_board.DisplayTetromino(j)

        if not self.game_over and not self.LiveTetromino.stopped:
            self.tetris_board.fall_tetromino(self.LiveTetromino)

        elif not self.game_over:
             self.tetrominos.append(self.LiveTetromino)
             self.create_next_live_tetromino(self.NextTetromino)
             self.NextTetromino = random.randint(1, 7)


    def createNextTetromino(self, NextTetromino):

        if self.NextTetromino == 1:
            tetrimino1 = Image(source="TetrominoO.png")
            self.next_piece_image(self.NextTetromino, tetrimino1)
        elif self.NextTetromino == 2:
            tetrimino2 = Image(source="TetrominoI.png")
            self.next_piece_image(self.NextTetromino, tetrimino2)
        elif self.NextTetromino == 3:
            tetrimino3 = Image(source="TetrominoT.png")
            self.next_piece_image(self.NextTetromino, tetrimino3)
        elif self.NextTetromino == 4:
            tetrimino4 = Image(source="TetrominoS.png")
            self.next_piece_image(self.NextTetromino, tetrimino4)
        elif self.NextTetromino == 5:
            tetrimino5 = Image(source="TetrominoZ.png")
            self.next_piece_image(self.NextTetromino, tetrimino5)
        elif self.NextTetromino == 6:
            tetrimino6 = Image(source="TetrominoJ.png")
            self.next_piece_image(self.NextTetromino, tetrimino6)
        elif self.NextTetromino == 7:
            tetrimino7 = Image(source="TetrominoL.png")
            self.next_piece_image(self.NextTetromino, tetrimino7)

    def create_next_live_tetromino(self, rand):
        if (rand == 1):
            self.LiveTetromino = TetrominoO()
        elif (rand == 2):
            self.LiveTetromino = TetrominoI()
        elif (rand == 3):
            self.LiveTetromino = TetrominoT()
        elif (rand == 4):
            self.LiveTetromino = TetrominoS()
        elif (rand == 5):
            self.LiveTetromino = TetrominoZ()
        elif (rand == 6):
            self.LiveTetromino = TetrominoJ()
        elif (rand == 7):
            self.LiveTetromino = TetrominoL()

    def on_key_down(self, keyboard, keycode, text, modifiers):
        if not self.game_over:
            if keycode == (115, 's'):
                self.calculate_down_collisions()
                if self.LiveTetromino.stopped == False:
                    self.tetris_board.fall_tetromino(self.LiveTetromino)
                    self.ScoreLabel.add_score(1)

            if keycode == (97, 'a'):
                self.LiveTetromino.stopped = False
                if not self.calculate_left_collisions():
                    self.tetris_board.move_left_tetromino(self.LiveTetromino)

            if keycode == (100, 'd'):
                self.LiveTetromino.stopped = False
                if not self.calculate_right_collisions():
                    self.tetris_board.move_right_tetromino(self.LiveTetromino)

            if keycode == (107, 'k'):
                self.tetris_board.blank_tetromino(self.LiveTetromino)
                self.LiveTetromino.rotate_right()
                if self.rotation_collision():
                    self.LiveTetromino.rotate_left()
                self.tetris_board.DisplayTetromino(self.LiveTetromino)

            if keycode == (106, 'j'):
                self.tetris_board.blank_tetromino(self.LiveTetromino)
                self.LiveTetromino.rotate_left()
                if self.rotation_collision():
                    self.LiveTetromino.rotate_right()
                self.tetris_board.DisplayTetromino(self.LiveTetromino)


    def on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def rotation_collision(self):
        collision = False
        for i in self.LiveTetromino.TetrominoLocation:
            if i[1] > 9 or i[1] < 0 or i[0] < 0 or i[0] > 19:
                collision = True
            if i[1] > 9 and i[1] == 0:
                collision = True

        for tetromino in self.tetrominos:
            for i in tetromino.TetrominoLocation:
                for j in self.LiveTetromino.TetrominoLocation:
                    if i[0] == j[0]:
                        if i[1] == j[1]:
                            collision = True
        return collision

    def calculate_left_collisions(self):
        for tetromino in self.tetrominos:
            for i in tetromino.TetrominoLocation:
                for j in self.LiveTetromino.TetrominoLocation:
                    if i[0] == j[0]:
                        if i[1] == j[1] - 1:
                            return True

    def calculate_right_collisions(self):
        for tetromino in self.tetrominos:
            for i in tetromino.TetrominoLocation:
                for j in self.LiveTetromino.TetrominoLocation:
                    if i[0] == j[0]:
                        if i[1] == j[1] + 1:
                            return True

    def calculate_down_collisions(self):
        for tetromino in self.tetrominos:
            for i in tetromino.TetrominoLocation:
                for j in self.LiveTetromino.TetrominoLocation:
                    if i[0] == j[0] + 1 and i[1] == j[1]:
                        self.LiveTetromino.stopped = True
        # check for hitting the bottom
        for i in self.LiveTetromino.TetrominoLocation:
            if (i[0] + 1 > 19):
                self.LiveTetromino.stopped = True
                return

    def calculate_game_over(self):

        if self.LiveTetromino.stopped and not self.game_over:
            for i in self.LiveTetromino.TetrominoLocation:
            #if self.LiveTetromino.TetrominoLocation[0][0] <= 1:
                if i[0] < 2:
                    self.game_over = True
                    self.checkScoreForLeaderBoard()
                    Clock.unschedule(self.clock)
                    print("GAME OVER")
                    print("The Leader Board: ")

                    count = 1
                    for i in self.Leaderboard:
                        print(str(count)+ ". " + str(i[0]) +" "+ str(i[1]))
                        count += 1
                    break


    def checkScoreForLeaderBoard(self):

        print("Enter User Name: ")
        self.Leaderboard.append([str(input()), self.ScoreLabel.return_score()])
        sortedLeaderboard = []
        for i in range(len(self.Leaderboard)):
            maxVal = None
            for j in self.Leaderboard:
                if maxVal == None:
                    maxVal = j
                elif j[1] > maxVal[1]:
                    maxVal = j
            sortedLeaderboard.append(maxVal)
            self.Leaderboard.remove(maxVal)
        #print(sortedLeaderboard)
        self.Leaderboard = sortedLeaderboard

        if len(self.Leaderboard) > 5:
            self.Leaderboard.pop()
    
class WindowManager(ScreenManager):
    Gamespeed = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Gamespeed = 2

    def start_clock(self):
        self.ids.GameBoard.set_clock(Clock.schedule_interval(self.ids.GameBoard.Update, 0.3)) #game speed



# This starts the main form and calls
TetrisWindow().run()
