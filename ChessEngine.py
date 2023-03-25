from ChessBoard import BoardState
from Pieces import *
from Rules import *

def implementMove(initPos, finalPos):
    if isValidMove(initPos, finalPos, False):
        pieceAtInitPos = BoardState[initPos[0]][initPos[1]]
        pieceAtFinalPos = BoardState[finalPos[0]][finalPos[1]]

        pieceAtInitPos.updateCurrPos( (finalPos[1], finalPos[0]) )
        if pieceAtFinalPos == null: # Empty cell
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )
        elif pieceAtFinalPos.color != pieceAtInitPos.color: # Capture
            pieceAtFinalPos.updateCurrPos(pieceAtFinalPos.ripPos)
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )

def generatePossibleMoves(initPos):
    moves = []

    for i in range(0, 8) :
        for j in range(0, 8):
            if isValidMove(initPos, (i, j), isUnderCheck()):
                moves.append((j, i))
    return moves