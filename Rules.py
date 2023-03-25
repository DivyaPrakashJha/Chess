from Pieces import *
from ChessBoard import *

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

def isUnderCheck():
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
            return False;
        else:
            return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 9:  # Queen
        if ( (initPos[0] != finalPos[0] and initPos[1] != finalPos[1]) and (abs(initPos[0]-finalPos[0]) != abs(initPos[1]-finalPos[1])) ):
            return False

        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 5:  # Rook
        if (initPos[0] != finalPos[0] and initPos[1] != finalPos[1]):
            return False
        else:
            increment = 1
            if (initPos[0] == finalPos[0]):
                if (initPos[1] > finalPos[1]):
                    increment = -1
                else:
                    increment = 1

                for i in range(initPos[1]+increment, finalPos[1]+increment, increment):
                    if (BoardState[finalPos[0]][i] != null):
                        return False

            elif (initPos[1] == finalPos[1]):
                if (initPos[0] > finalPos[0]):
                    increment = -1
                else:
                    increment = 1

                for i in range(initPos[0]+increment, finalPos[0]+increment, increment):
                    if (BoardState[i][finalPos[1]] != null):
                        return False


        return True
    # *******************************************************************************

    elif pieceAtInitPos.getPieceValue() == 3.2:  # Bishop
        if ( abs(initPos[0] - finalPos[0]) != abs(initPos[1] - finalPos[1] )):
            return False
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
        if (pieceAtInitPos.color == 'W'):
            if (initPos[1] != finalPos[1]):
                return False
            if (finalPos[0] < initPos[0]):
                return False
            if (initPos[0] == 1 and finalPos[0] > 3):
                return False
            elif (initPos[0] != 1 and finalPos[0] > initPos[0] + 1):
                return False
            return True
        elif (pieceAtInitPos.color == 'B'):
            if (initPos[1] != finalPos[1]):
                return False;
            if (finalPos[0] > initPos[0]):
                return False
            if (initPos[0] == 6 and finalPos[0] < 4):
                return False
            elif (initPos[0] != 6 and finalPos[0] < initPos[0] - 1):
                return False
            return True
    # *******************************************************************************

