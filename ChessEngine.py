from ChessBoard import BoardState
from Pieces import *

def implementMove(initPos, finalPos):
    pieceAtInitPos = BoardState[initPos[0]][initPos[1]]
    pieceAtFinalPos = BoardState[finalPos[0]][finalPos[1]]

    if pieceAtInitPos.isValidMove():
        pieceAtInitPos.updateCurrPos( (finalPos[1], finalPos[0]) );
        if pieceAtFinalPos == null: # Empty cell
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )
        elif pieceAtFinalPos.color != pieceAtInitPos.color: # Capture
            pieceAtFinalPos.updateCurrPos(pieceAtFinalPos.ripPos)
            ( BoardState[initPos[0]][initPos[1]] , BoardState[finalPos[0]][finalPos[1]] ) = (null, BoardState[initPos[0]][initPos[1]] )
