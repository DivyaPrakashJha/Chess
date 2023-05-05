from Pieces import *

# Colors
grey = ((110, 110, 110), (255, 255, 255)) # (black, white)
green = ((119, 149, 86), (235, 236, 208))
brown = ((181, 136, 99), (240, 217, 181))
blue = ((107, 149, 187), (200, 222, 253))

# Square size
side = 90
class Board:
    def __init__(self, side, color, height, width):
        self.side = side
        self.color = color
        self.height = height
        self.width = width


board = Board(side, grey, side*8.5, side*12.5)


# Board State
BoardState = [
    [rookB1, knightB1, bishopBw, queenB, kingB, bishopBb, knightB2, rookB2],
    [pawnB1, pawnB2, pawnB3, pawnB4, pawnB5, pawnB6, pawnB7, pawnB8],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [null, null, null, null, null, null, null, null],
    [pawnW1, pawnW2, pawnW3, pawnW4, pawnW5, pawnW6, pawnW7, pawnW8],
    [rookW1, knightW1, bishopWb, queenW, kingW, bishopWw, knightW2, rookW2]
]
