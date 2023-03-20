import pyaudio
import speech_recognition


def getPosByVoice(turn, gameState):
    if (gameState == 0):
        return (1, 5)
    else:
        return (4, 5)