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
    ypos = pos[1] * side

    return (xpos, ypos)

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

# Game Font

bigGameFont = pygame.font.Font(gameFolder + 'GameFonts/SkaterDudes.ttf', 100)
medGameFont = pygame.font.Font(gameFolder + 'GameFonts/SkaterDudes.ttf', 70)
smallGameFont = pygame.font.Font(gameFolder + 'GameFonts/SkaterDudes.ttf', 40)

GREEN = pygame.Color(0,200,0)
RED = pygame.Color(255,0,0)
WHITE = pygame.Color(255,255,255)
BLACK = pygame.Color(0, 0, 0)
YELLOW = pygame.Color(255, 255, 0)

# ******************************************************************************

# Inputs
def takeMouseInput():
    location = pygame.mouse.get_pos()

    x = (location[0] - 2 * side) // side
    y = (location[1]) // side

    return (y, x)

def takeVoiceInput():
    (x, y) = getPosition()

    # conf = SpeechToText();
    # if (conf == "yes" or conf == "as"):
    #     return (y, x)

    return (y, x)
# ******************************************************************************

# Game

clock = pygame.time.Clock();
FPS = 20
gameMode = 2  # 1 -> Single Player (vs engine) 2 -> Two Players
boardStyle = 1

# ******************************************************************************

# StartScreen
def start():
    select = False
    coverImage = pygame.image.load(gameFolder + "GameImages/CoverImage.jpg")
    coverImage = pygame.transform.scale(coverImage, (width, height))

    surface.blit(coverImage, (0, 0))
    title = bigGameFont.render("The Game of Wits", True, YELLOW)
    titleRect = title.get_rect()
    titleRect.centerx = width//2
    titleRect.centery = height//3

    playGame = medGameFont.render("Play", True, GREEN);
    playRect = playGame.get_rect()
    playRect.centerx = width // 4
    playRect.centery = height // 1.6

    quitGame = medGameFont.render("Quit", True, RED);
    quitRect = playGame.get_rect()
    quitRect.centerx = width // 1.33
    quitRect.centery = height // 1.6

    surface.blit(title, titleRect)
    surface.blit(playGame, playRect)
    surface.blit(quitGame, quitRect);

    choice = 0

    while not select:
        x, y = pygame.mouse.get_pos()

        if (x >= playRect[0] and x <= playRect[0] + playRect.width) and (y >= playRect[1] and y <= playRect[1] + playRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 1
        elif (x >= quitRect[0] and x <= quitRect[0]+quitRect.width) and (y >= quitRect[1] and y <= quitRect[1]+quitRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 2
        else:
            pygame.mouse.set_cursor(pygame.cursors.ball)
            choice = 0

        for evnt in pygame.event.get():
            if (evnt.type == pygame.QUIT):
                select = True
            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_ESCAPE:
                    select = True

            if (evnt.type == pygame.MOUSEBUTTONDOWN):
                if choice:
                    select = True

        pygame.display.update()
        clock.tick(FPS)

    if (choice == 1):
        chooseMode()
# ******************************************************************************

# Select Mode Screen
def chooseMode():
    select = False
    coverImage = pygame.image.load(gameFolder + "GameImages/CoverImage.jpg")
    coverImage = pygame.transform.scale(coverImage, (width, height))

    surface.blit(coverImage, (0, 0))

    back = smallGameFont.render("-BACK-", True, RED)
    backRect = back.get_rect()
    backRect.x = 0
    backRect.y = 0

    chPlayer = bigGameFont.render("Choose Mode", True, GREEN)
    chPlayerRect = chPlayer.get_rect()
    chPlayerRect.centerx = width // 2
    chPlayerRect.centery = height // 4

    onePlayer = medGameFont.render("1 Player", True, WHITE)
    onePlayerRect = onePlayer.get_rect()
    onePlayerRect.centerx = width // 2
    onePlayerRect.centery = height // 2

    twoPlayers = medGameFont.render("2 Players", True, WHITE)
    twoPlayersRect = twoPlayers.get_rect()
    twoPlayersRect.centerx = width // 2
    twoPlayersRect.centery = height // 1.3

    surface.blit(back, backRect)
    surface.blit(chPlayer, chPlayerRect)
    surface.blit(onePlayer, onePlayerRect)
    surface.blit(twoPlayers, twoPlayersRect)

    choice = 0

    while not select:
        x, y = pygame.mouse.get_pos()

        if (x >=  onePlayerRect[0] and x <= onePlayerRect[0] + onePlayerRect.width) and (y >= onePlayerRect[1] and y <= onePlayerRect[1] + onePlayerRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 1
        elif (x >= twoPlayersRect[0] and x <= twoPlayersRect[0] + twoPlayersRect.width) and (y >= twoPlayersRect[1] and y <= twoPlayersRect[1] + twoPlayersRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 2
        elif (x >= backRect[0] and x <= backRect[0] + backRect.width) and (y >= backRect[1] and y <= backRect[1] + backRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 3
        else:
            pygame.mouse.set_cursor(pygame.cursors.ball)
            choice = 0

        for evnt in pygame.event.get():
            if (evnt.type == pygame.QUIT):
                select = True
            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_ESCAPE:
                    select = True

            if (evnt.type == pygame.MOUSEBUTTONDOWN):
                if choice:
                    select = True
        pygame.display.update()
        clock.tick(FPS)

    if choice == 3:
        start()
    elif choice != 0:
        gameMode = choice
        chooseBoardStyle()
# ******************************************************************************
def chooseBoardStyle():
    select = False
    coverImage = pygame.image.load(gameFolder + "GameImages/CoverImage.jpg")
    coverImage = pygame.transform.scale(coverImage, (width, height))

    surface.blit(coverImage, (0, 0))

    back = smallGameFont.render("-BACK-", True, RED)
    backRect = back.get_rect()
    backRect.x = 0
    backRect.y = 0

    chBoard = bigGameFont.render("Select Board", True, GREEN)
    chBoardRect = chBoard.get_rect()
    chBoardRect.centerx = width // 2
    chBoardRect.centery = height // 2

    surface.blit(back, backRect)
    surface.blit(chBoard, chBoardRect)

    choice = 0

    while not select:
        x, y = pygame.mouse.get_pos()

        if (x >= backRect[0] and x <= backRect[0] + backRect.width) and (y >= backRect[1] and y <= backRect[1] + backRect.height):
            pygame.mouse.set_cursor(pygame.cursors.diamond)
            choice = 5

        for evnt in pygame.event.get():
            if (evnt.type == pygame.QUIT):
                select = True
            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_ESCAPE:
                    select = True

            if (evnt.type == pygame.MOUSEBUTTONDOWN):
                if choice:
                    select = True
        pygame.display.update()
        clock.tick(FPS)

    if choice == 5:
        chooseMode()
    else:
        pygame.mixer.music.stop()
        game()
# ******************************************************************************
def endScreen(winner):
    select = False
    coverImage = pygame.image.load(gameFolder + "GameImages/CoverImage.jpg")
    coverImage = pygame.transform.scale(coverImage, (width, height))

    surface.blit(coverImage, (0, 0))

    win = bigGameFont.render(winner + " Wins!!", True, WHITE)
    winRect = win.get_rect()
    winRect.centerx = width // 2
    winRect.centery = height // 2

    surface.blit(win, winRect)

    while not select:
        for evnt in pygame.event.get():
            if (evnt.type == pygame.QUIT):
                select = True
            if (evnt.type == pygame.KEYDOWN):
                if evnt.key == pygame.K_ESCAPE:
                    play = False

        pygame.display.update()
        clock.tick(FPS)

def game():
    play = True
    assetsLoaded = False
    initPos = []
    finalPos = []

    turn = 0  # 0 -> White's Turn, 1 -> Black's Turn
    gameState = 0  # 0 -> Select Initial Position, 1 -> Select Final Position for Piece

    while(play):
        if not assetsLoaded:
            backgroundImage = pygame.image.load(gameFolder + "GameImages/gameBackground.png");
            backgroundImage = pygame.transform.scale(backgroundImage, (width, height))
            surface.blit(backgroundImage, (0, 0))

            assetsLoaded = True
            wTurn.play()

        displayBoard()
        displayWhitePieces()
        displayBlackPieces()

        if gameState == 1:
            displaySrcSquare((initPos[1], initPos[0]))
            displayPossibleMoves(initPos)


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

                            pygame.time.wait(1100)
                            src.play()

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

                                pygame.time.wait(1100)
                                src.play()


        pygame.display.update()
        clock.tick(FPS)


def main():
    pygame.mixer.music.load(gameFolder + "GameSounds/instrumental.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()
    start()
    # endScreen("White")

main()
pygame.quit();

