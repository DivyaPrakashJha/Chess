# Packages
import pygame
import math
import time
# *******************************************************************************

# Modules
from ChessBoard import *
from Pieces import *
from ChessEngine import *
from VoiceRecognition import *
# *******************************************************************************
pygame.init();

# Game Location
gameFolder = "D:/SE/PBL2/"
# *******************************************************************************

# Game Window and Title
surface = pygame.display.set_mode( (width, height) );
pygame.display.set_caption('Game of Wits')
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

    for x in moves:
        posMove = pygame.image.load(gameFolder + "GameImages/greenCircleSmall.png")
        posMove = pygame.transform.scale(posMove, (side, side))
        surface.blit(posMove, getPosOnScreen(x))
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


# Game

play = True
assetsLoaded = False
clock = pygame.time.Clock();
FPS = 20

turn = 0 # 0 -> White's Turn, 1 -> Black's Turn
gameState = 0 # 0 -> Select Initial Position, 1 -> Select Final Position for Piece
initPos = () # For a move
finalPos = ()

while(play):
    if not assetsLoaded:
        backgroundImage = pygame.image.load(gameFolder + "GameImages/gameBackground.png");
        backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
        surface.blit(backgroundImage, (0, 0))
        pygame.mixer.music.load(gameFolder + "GameSounds/instrumental.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

        assetsLoaded = True

    displayBoard()
    displayWhitePieces()
    displayBlackPieces()

    for evnt in pygame.event.get():
        if (evnt.type == pygame.QUIT):
            play = False
        if (evnt.type == pygame.MOUSEBUTTONDOWN): # For moving pieces through mouse
            location = pygame.mouse.get_pos();

            x = (location[0] - 2*side)//side
            y = (location[1] - side)//side;

            if not (len(initPos) == 0 and BoardState[y][x] == null):
                if len(initPos) == 0:
                    initPos = (y, x)
                    displaySrcSquare( (x, y) )
                    displayPossibleMoves( initPos )

                    dest.play()
                elif (y == initPos[0] and x == initPos[1]):
                    initPos = ()
                else:
                    finalPos = (y, x)
                    print(initPos, finalPos)
                    implementMove(initPos, finalPos)
                    src.play()
                    initPos = ()
                    finalPos = ()
        if (evnt.type == pygame.KEYDOWN):
            if evnt.key == pygame.K_ESCAPE:
                play = False
            if evnt.key == pygame.K_SPACE:
                if (gameState == 0):
                    initPos = getPosByVoice(turn, gameState)
                    gameState+=1
                elif (gameState == 1):
                    finalPos = getPosByVoice(turn, gameState)
                    implementMove(initPos, finalPos);
                    initPos = ()
                    finalPos = ()
                    gameState-=1


    pygame.display.update()
    clock.tick(FPS)


pygame.quit();

