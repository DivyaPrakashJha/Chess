# Packages
import pygame
import math
import time
# *******************************************************************************

# Game Location
gameFolder = "D:/SE/PBL2/"
# *******************************************************************************

# Modules
from ChessBoard import *
from Pieces import *
from ChessEngine import *
from VoiceRecognition import *
# *******************************************************************************

pygame.init();

# Game Window and Title
surface = pygame.display.set_mode( (width, height) );
pygame.display.set_caption('The  Game of Wits')
# *******************************************************************************

# Display of Board Configuration
def getPosOnScreen(pos): # from x, y coordinates
    xpos = 2*side + pos[0] * side
    ypos = side + pos[1] * side

    return (xpos, ypos)

# Function for displaying a cell
def printBlackSquare(x, y):
    pygame.draw.rect(surface, black, pygame.Rect(x, y, side, side));
def printWhiteSquare(x, y):
    pygame.draw.rect(surface, white, pygame.Rect(x, y, side, side));

# Function for displaying the board
def displayBoard():
    x = -side
    y = 0
    for i in range(1, 9):
        y += side
        x = -side
        for j in range(1, 13):
            x += side
            if (j <= 2 or j >= 11):
                continue
            if (i+j)%2 == 0:
                printWhiteSquare(x, y);
            else:
                printBlackSquare(x, y);

# Function for displaying the white pieces
def displayWhitePieces():
    for pi in whitePieces: # displaying white pieces
        Image = pygame.image.load(gameFolder + pi.getLogo())
        Image = pygame.transform.scale(Image, (side, side))
        surface.blit(Image, getPosOnScreen(pi.currPos))

# Function for displaying the black pieces
def displayBlackPieces():
    for pi in blackPieces: # displaying black pieces
        Image = pygame.image.load(gameFolder + pi.getLogo())
        Image = pygame.transform.scale(Image, (side, side))
        surface.blit(Image, getPosOnScreen(pi.currPos))

# Function for displaying the selected piece
def displaySrcSquare(src):
    selBox = pygame.image.load(gameFolder + "GameImages/yellowBox.png")
    selBox = pygame.transform.scale(selBox, (side, side))
    surface.blit(selBox, getPosOnScreen(src))

# Function for displaying the possible moves
def displayPossibleMoves(src):
    moves = generatePossibleMoves(src);

    for cord in moves:
        posMove = pygame.image.load(gameFolder + "GameImages/greenCircleSmall.png")
        posMove = pygame.transform.scale(posMove, (side, side))
        surface.blit(posMove, getPosOnScreen(cord))
# *******************************************************************************

# Game Sounds

wTurn = pygame.mixer.Sound(gameFolder + "GameSounds/whiteturn.wav")
wTurn.set_volume(0.8)
bTurn = pygame.mixer.Sound(gameFolder + "GameSounds/blackturn.wav")
bTurn.set_volume(0.8)
src = pygame.mixer.Sound(gameFolder + 'GameSounds/selectpiece.wav')
src.set_volume(0.8)
dest = pygame.mixer.Sound(gameFolder + 'GameSounds/destination.wav')
dest.set_volume(0.8)
# ******************************************************************************

# Inputs
def takeMouseInput():
    location = pygame.mouse.get_pos()

    x = (location[0] - 2 * side) // side
    y = (location[1] - side) // side

    return (y, x)

def takeVoiceInput():
    (x, y) = getPosition()

    # conf = SpeechToText();
    # if (conf == "yes" or conf == "as"):
    #     return (y, x)

    return (y, x)
# ******************************************************************************

# Game

play = True
assetsLoaded = False
clock = pygame.time.Clock();
FPS = 20
initPos = []
finalPos = []

turn = 0 # 0 -> White's Turn, 1 -> Black's Turn
gameState = 0 # 0 -> Select Initial Position, 1 -> Select Final Position for Piece


while(play):
    if not assetsLoaded:
        backgroundImage = pygame.image.load(gameFolder + "GameImages/gameBackground.png");
        backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
        surface.blit(backgroundImage, (0, 0))
        # pygame.mixer.music.load(gameFolder + "GameSounds/instrumental.mp3")
        # pygame.mixer.music.set_volume(0.4)
        # pygame.mixer.music.play()

        assetsLoaded = True
        wTurn.play()

    displayBoard()
    displayWhitePieces()
    displayBlackPieces()

    if gameState == 1:
        displaySrcSquare((initPos[1], initPos[0]))
        # displayPossibleMoves(initPos)


    for evnt in pygame.event.get():
        if (evnt.type == pygame.QUIT):
            play = False
        if (evnt.type == pygame.KEYDOWN):
            if evnt.key == pygame.K_ESCAPE:
                play = False

        if (gameState == 0):
            if (evnt.type == pygame.MOUSEBUTTONDOWN): # For moving pieces through mouse
                initPos = takeMouseInput()
                print(initPos)

                if isValidSrc(initPos, turn):
                    displaySrcSquare( (initPos[1], initPos[0]) )
                    displayPossibleMoves(initPos)
                    gameState = 1

                    dest.play()

            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_SPACE:
                    initPos = takeVoiceInput()

                    if isValidSrc(initPos, turn):
                        displaySrcSquare((initPos[1], initPos[0]))
                        displayPossibleMoves(initPos)
                        gameState = 1

                        dest.play()

        elif (gameState == 1):
            if (evnt.type == pygame.MOUSEBUTTONDOWN):
                finalPos = takeMouseInput()
                if finalPos == initPos:
                    gameState = 0
                else:
                    if implementMove(initPos, finalPos) == True:
                        gameState = 0
                        turn = 1-turn


                        displayBoard()
                        displayWhitePieces()
                        displayBlackPieces()
                        pygame.display.update()
                        clock.tick(FPS)

                        pygame.time.wait(1100)
                        if (turn == 0):
                            wTurn.play()
                        else:
                            bTurn.play()


            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_SPACE:
                    finalPos = takeVoiceInput()
                    if finalPos == initPos:
                        gameState = 0
                    else:
                        if implementMove(initPos, finalPos) == True:
                            gameState = 0
                            turn = 1 - turn
                            if (turn == 0):
                                wTurn.play()
                            else:
                                bTurn.play()
                            # pygame.time.wait(1100)
                            # src.play()

    pygame.display.update()
    clock.tick(FPS)


pygame.quit();

