# **** Classes ****

class King:
    def __init__(self, color, currPos,  ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhiteKing.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackKing.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos

    def getPieceValue(self):
        return 99

# *******************************************************************************
class Queen:
    def __init__(self, color, currPos, ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhiteQueen.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackQueen.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos;

    def getPieceValue(self):
        return 9

# *******************************************************************************
class Rook:
    def __init__(self, color, currPos, ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhiteRook.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackRook.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos;

    def getPieceValue(self):
        return 5

# *******************************************************************************
class Bishop:
    def __init__(self, color, currPos, ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhiteBishop.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackBishop.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos;

    def getPieceValue(self):
        return 3.2

    def isValidMove(finalPos):
        return True

# *******************************************************************************
class Knight:
    def __init__(self, color, currPos, ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhiteKnight.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackKnight.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos

    def getPieceValue(self):
        return 3

# *******************************************************************************
class Pawn:
    def __init__(self, color, currPos, ripPos):
        self.color = color
        self.currPos = currPos
        self.ripPos = ripPos

    def getLogo(self):
        if (self.color == 'W'):
            return "GameImages/ChessPieces/WhitePawn.png"
        elif (self.color == 'B'):
            return "GameImages/ChessPieces/BlackPawn.png"

    def updateCurrPos(self, newPos):
        self.currPos = newPos;

    def getPieceValue(self):
        return 1

# *******************************************************************************
class Null: # for empty cell
    def __init__(self, points = 0):
        self.points = 0

# *******************************************************************************

# Pieces as Objects

whitePieces = []
deadWhitePieces = []

kingW = King('W', (4, 7), (9.25, 4))
queenW = Queen('W', (3, 7), (9.25, 3))
bishopWb = Bishop('W', (2, 7), (9.25, 2))
bishopWw = Bishop('W', (5, 7), (9.25, 5))
knightW1 = Knight('W', (1, 7), (9.25, 1))
knightW2 = Knight('W', (6, 7), (9.25, 6))
rookW1 = Rook('W', (0, 7), (9.25, 0))
rookW2 = Rook('W', (7, 7), (9.25, 7))
pawnW1 = Pawn('W', (0, 6), (8.25, 0))
pawnW2 = Pawn('W', (1, 6), (8.25, 1))
pawnW3 = Pawn('W', (2, 6), (8.25, 2))
pawnW4 = Pawn('W', (3, 6), (8.25, 3))
pawnW5 = Pawn('W', (4, 6), (8.25, 4))
pawnW6 = Pawn('W', (5, 6), (8.25, 5))
pawnW7 = Pawn('W', (6, 6), (8.25, 6))
pawnW8 = Pawn('W', (7, 6), (8.25, 7))

whitePieces.append(kingW)
whitePieces.append(queenW)
whitePieces.append(bishopWw)
whitePieces.append(bishopWb)
whitePieces.append(knightW1)
whitePieces.append(knightW2)
whitePieces.append(rookW1)
whitePieces.append(rookW2)
whitePieces.append(pawnW1)
whitePieces.append(pawnW2)
whitePieces.append(pawnW3)
whitePieces.append(pawnW4)
whitePieces.append(pawnW5)
whitePieces.append(pawnW6)
whitePieces.append(pawnW7)
whitePieces.append(pawnW8)

blackPieces = []
deadBlackPieces = []

kingB = King('B', (4, 0), (-2.25, 4))
queenB = Queen('B', (3, 0), (-2.25, 3))
bishopBw = Bishop('B', (2, 0), (-2.25, 2))
bishopBb = Bishop('B', (5, 0), (-2.25, 5))
knightB1 = Knight('B', (1, 0), (-2.25, 1))
knightB2 = Knight('B', (6, 0), (-2.25, 6))
rookB1 = Rook('B', (0, 0), (-2.25, 0))
rookB2 = Rook('B', (7, 0), (-2.25, 7))
pawnB1 = Pawn('B', (0, 1), (-1.25, 0))
pawnB2 = Pawn('B', (1, 1), (-1.25, 1))
pawnB3 = Pawn('B', (2, 1), (-1.25, 2))
pawnB4 = Pawn('B', (3, 1), (-1.25, 3))
pawnB5 = Pawn('B', (4, 1), (-1.25, 4))
pawnB6 = Pawn('B', (5, 1), (-1.25, 5))
pawnB7 = Pawn('B', (6, 1), (-1.25, 6))
pawnB8 = Pawn('B', (7, 1), (-1.25, 7))

blackPieces.append(kingB)
blackPieces.append(queenB)
blackPieces.append(bishopBw)
blackPieces.append(bishopBb)
blackPieces.append(knightB1)
blackPieces.append(knightB2)
blackPieces.append(rookB1)
blackPieces.append(rookB2)
blackPieces.append(pawnB1)
blackPieces.append(pawnB2)
blackPieces.append(pawnB3)
blackPieces.append(pawnB4)
blackPieces.append(pawnB5)
blackPieces.append(pawnB6)
blackPieces.append(pawnB7)
blackPieces.append(pawnB8)

null = Null(0) # Empty Space