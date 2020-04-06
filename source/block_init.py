from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt

class Tango_block:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class ScreenObject(Tango_block):
    def __init__(self, name, x, y, id, minmax, mp3):
        super().__init__(name, id)
        self.size = [x, y]
        self.minmax = minmax
        self.mp3 = mp3

class BlockObject(Tango_block):
    def __init__(self, name, x, y, id):
        super().__init__(name, id)
        self.size = [x, y]
        self.alias = name

class QuestionObject(Tango_block):
    def __init__(self, name, id, color):
        super().__init__(name, id)
        self.pos = [1, 1]
        self.color = color
        self.blocks = []

class AnswerObject(Tango_block):
    def __init__(self, name, id, color, blocks):
        super().__init__(name, id)
        self.pos = [1, 1]
        self.color = color
        self.blocks = blocks

class Mp3Object(Tango_block):
    def __init__(self, name, mp3):
        self.name = name
        self.mp3 = mp3