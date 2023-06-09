from ChessBoard import BoardState
from Pieces import *

def isValidSrc(src, turn):
    if (src[0] > 7 or src[1] > 7 or src[0] < 0 or src[1] < 0):
        return False
    elif BoardState[src[0]][src[1]] == null:
        return False
    elif turn == 0 and BoardState[src[0]][src[1]].color == 'B':
        return False
    elif turn == 1 and BoardState[src[0]][src[1]].color == 'W':
        return False

    return True


def isUnderCheck(turn):
    if turn == 0:
        kpos = kingW.currPos
        for piece in blackPieces:
            if (isValidMove((piece.currPos[1], piece.currPos[0]), (kpos[1], kpos[0]), False)):
                return True
    elif turn == 1:
        kpos = kingB.currPos
        for piece in whitePieces:
            if (isValidMove((piece.currPos[1], piece.currPos[0]), (kpos[1], kpos[0]), False)):
                return True
    return False

def checkEvasion(turn):
    return True

def isCheckMate(turn):
    boardcopy = BoardState

    if checkEvasion(turn):
        return False
    elif isUnderCheck(turn):
        if turn == 0:
            x = generatePossibleMoves((kingW.currPos[1], kingW.currPos[0]), turn)
            if len(x) == 0:
                return True
        else:
            x = generatePossibleMoves((kingB.currPos[1], kingB.currPos[0]), turn)
            if len(x) == 0:
                return True
    return False

def isValidMove(initPos, finalPos, isUnderCheck):
    pieceAtInitPos = BoardState[initPos[0]][initPos[1]]
    pieceAtFinalPos = BoardState[finalPos[0]][finalPos[1]]

    # *******************************************************************************

    if (finalPos[0] > 7 or finalPos[0] < 0 or finalPos[1] > 7 or finalPos[1] < 0):
        return False;
    if pieceAtFinalPos != null and pieceAtInitPos.color == pieceAtFinalPos.color:
        return False
    # *******************************************************************************

    if pieceAtInitPos.getPieceValue() == 99:  # King
        if (abs(finalPos[0] - initPos[0]) > 1 or abs(finalPos[1] - initPos[1]) > 1):
            return False
        else:
            if pieceAtInitPos.color == 'W':
                for piece in blackPieces:
                    if isValidMove((piece.currPos[1], piece.currPos[0]), finalPos, False):
                        return False
            else:
                for piece in whitePieces:
                    if isValidMove((piece.currPos[1], piece.currPos[0]), finalPos, False):
                        return False
        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 9:  # Queen
        if ( (initPos[0] != finalPos[0] and initPos[1] != finalPos[1]) and (abs(initPos[0]-finalPos[0]) != abs(initPos[1]-finalPos[1])) ):
            return False
        else:
            xincrement = 0
            yincrement = 0

            if (initPos[0] < finalPos[0]):
                xincrement = 1
            elif (initPos[0] > finalPos[0]):
                xincrement = -1

            if (initPos[1] < finalPos[1]):
                yincrement = 1
            elif (initPos[1] > finalPos[1]):
                yincrement = -1

            i = initPos[0] + xincrement
            j = initPos[1] + yincrement

            while (i != finalPos[0] or j != finalPos[1]):
                if (BoardState[i][j] != null):
                    return False
                i += xincrement
                j += yincrement

        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 5:  # Rook
        if (initPos[0] != finalPos[0] and initPos[1] != finalPos[1]):
            return False
        else:
            xincrement = 0
            yincrement = 0

            if (initPos[0] < finalPos[0]):
                xincrement = 1
            elif (initPos[0] > finalPos[0]):
                xincrement = -1

            if (initPos[1] < finalPos[1]):
                yincrement = 1
            elif (initPos[1] > finalPos[1]):
                yincrement = -1

            i = initPos[0] + xincrement
            j = initPos[1] + yincrement

            while (i != finalPos[0] or j != finalPos[1]):
                if (BoardState[i][j] != null):
                    return False
                i += xincrement
                j += yincrement

        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 3.2:  # Bishop
        if ( abs(initPos[0] - finalPos[0]) != abs(initPos[1] - finalPos[1] )):
            return False
        else:
            if (initPos[0] < finalPos[0]):
                xincrement = 1
            else:
                xincrement = -1

            if (initPos[1] < finalPos[1]):
                yincrement = 1
            else:
                yincrement = -1

            i = initPos[0] + xincrement
            j = initPos[1] + yincrement

            while i != finalPos[0]:
                if (BoardState[i][j] != null):
                    return False
                i += xincrement
                j += yincrement

        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 3:  # Knight
        pos1 = (initPos[0]+2, initPos[1]+1)
        pos2 = (initPos[0]+2, initPos[1]-1)
        pos3 = (initPos[0]-2, initPos[1]+1)
        pos4 = (initPos[0]-2, initPos[1]-1)
        pos5 = (initPos[0]+1, initPos[1]+2)
        pos6 = (initPos[0]-1, initPos[1]+2)
        pos7 = (initPos[0]+1, initPos[1]-2)
        pos8 = (initPos[0]-1, initPos[1]-2)

        pos =  []
        pos = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]


        for x in pos:
            if (x[0] < 8 and x[0] >= 0):
                if (finalPos[0] == x[0] and finalPos[1] == x[1]):
                    return True

        return False
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 1:  # Pawn
        if (pieceAtInitPos.color == 'B'): # Take
            if (finalPos[0] == initPos[0]+1 and (finalPos[1] == initPos[1]+1 or finalPos[1] == initPos[1]-1) ):
                if (BoardState[finalPos[0]][finalPos[1]] != null):
                    return True
            if (finalPos[0] == initPos[0]+1 and BoardState[finalPos[0]][finalPos[1]] != null):
                return False
            if (initPos[1] != finalPos[1]):
                return False
            if (finalPos[0] < initPos[0]):
                return False
            if (initPos[0] == 1):
                if finalPos[0] > 3:
                    return False
                if (BoardState[2][finalPos[1]] != null):
                    return False
                if (finalPos[0] == 3 and BoardState[3][finalPos[1]] != null):
                    return False
            elif (initPos[0] != 1 and finalPos[0] > initPos[0] + 1):
                return False
            return True
        elif (pieceAtInitPos.color == 'W'):
            if (finalPos[0] == initPos[0]-1 and (finalPos[1] == initPos[1]+1 or finalPos[1] == initPos[1]-1) ):
                if (BoardState[finalPos[0]][finalPos[1]] != null):
                    return True
            if (finalPos[0] == initPos[0]-1 and BoardState[finalPos[0]][finalPos[1]] != null):
                return False
            if (initPos[1] != finalPos[1]):
                return False;
            if (finalPos[0] > initPos[0]):
                return False
            if (initPos[0] == 6):
                if finalPos[0] < 4:
                    return False
                if (BoardState[5][finalPos[1]] != null):
                    return False
                if (finalPos[0] == 4 and BoardState[4][finalPos[1]] != null):
                    return False
            elif (initPos[0] != 6 and finalPos[0] < initPos[0] - 1):
                return False
            return True
    # *******************************************************************************


def implementMove(initPos, finalPos):
    if BoardState[initPos[0]][initPos[1]].color == 'W':
        turn = 0
    else:
        turn = 1

    if isValidMove(initPos, finalPos, isUnderCheck(turn)):
        pieceAtInitPos = BoardState[initPos[0]][initPos[1]]
        pieceAtFinalPos = BoardState[finalPos[0]][finalPos[1]]

        pieceAtInitPos.updateCurrPos( (finalPos[1], finalPos[0]) )
        if pieceAtFinalPos == null: # Empty cell
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )
        elif pieceAtFinalPos.color != pieceAtInitPos.color: # Capture
            pieceAtFinalPos.updateCurrPos(pieceAtFinalPos.ripPos)
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )
            if pieceAtFinalPos.color == 'W':
                deadWhitePieces.append(pieceAtFinalPos)
                whitePieces.remove(pieceAtFinalPos)
            if pieceAtFinalPos.color == 'B':
                blackPieces.remove(pieceAtFinalPos)
                deadBlackPieces.append(pieceAtFinalPos)

        return True
    return False

def generatePossibleMoves(initPos, turn):
    moves = []

    for i in range(0, 8) :
        for j in range(0, 8):
            if isValidMove(initPos, (i, j), isUnderCheck(turn)):
                moves.append((j, i))
    return moves