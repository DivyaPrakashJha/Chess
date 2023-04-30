from Pieces import *

# Square size
side = 80

# Colors
black = (110, 110, 110); # to depict black
white = (255, 255, 255);

# Board Size
height = side*10
width = side*12

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
