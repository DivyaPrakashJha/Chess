# Packages
import pygame
import chess
import time
import speech_recognition as sr
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
pygame.display.set_caption('Voice-Chess')

backgroundImage = pygame.image.load(gameFolder + "GameImages/gameBackground.png");
backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
surface.blit(backgroundImage, (0, 0))
# *******************************************************************************

# Display of Board Configuration

# Function for displaying a cell
def printBlackSquare(x, y):
    pygame.draw.rect(surface, black, pygame.Rect(x, y, side, side));
def printWhiteSquare(x, y):
    pygame.draw.rect(surface, white, pygame.Rect(x, y, side, side));

# Function for displaying the board
def displayBoard():
    x = -side
    y = -side

    for i in range(1, 9):
        y += side
        x = -side
        for j in range(1, 13):
            x += side
            if (j <= 2):
                continue
            elif (j >= 11):
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
        xpos = 2*side + pi.currPos[0] * side
        ypos = pi.currPos[1] * side
        surface.blit(Image, (xpos, ypos))

# Function for displaying the black pieces
def displayBlackPieces():
    for pi in blackPieces: # displaying black pieces
        Image = pygame.image.load(gameFolder + pi.getLogo())
        Image = pygame.transform.scale(Image, (side, side))
        xpos = 2*side + pi.currPos[0]  * side
        ypos = pi.currPos[1] * side
        surface.blit(Image, (xpos, ypos))


# *******************************************************************************


# Game

play = True
clock = pygame.time.Clock();
FPS = 10
turn = 0 # 0 -> White's Turn, 1 -> Black's Turn
initPos = ()
finalPos = ()
timer = 0;

while(play):
    displayBoard()
    displayWhitePieces()
    displayBlackPieces()

    for evnt in pygame.event.get():
        if (evnt.type == pygame.QUIT):
            play = False
        if (evnt.type == pygame.MOUSEBUTTONDOWN):
            location = pygame.mouse.get_pos();

            x = (location[0] - 2*side)//side
            y = (location[1])//side;

            if not (len(initPos) == 0 and BoardState[y][x] == null):
                if len(initPos) == 0:
                    initPos = (y, x)
                elif (y == initPos[0] and x == initPos[1]):
                    initPos = ()
                else:
                    finalPos = (y, x)
                    implementMove(initPos, finalPos);
                    initPos = ()
                    finalPos = ()

    pygame.display.update()
    clock.tick(FPS)


pygame.quit();

