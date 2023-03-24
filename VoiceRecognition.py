import speech_recognition as sr
import time

# def speechToText():
    # recognizer = sr.Recognizer()
    #
    # try:
    #     with sr.Microphone() as mic:
    #         print("Speak..")
    #         recognizer.adjust_for_ambient_noise(mic, duration = 0.1)
    #         audio = recognizer.listen(mic)
    #         print("Recognizing..")
    #         text = recognizer.recognize_ibm(audio)
    #
    #         return text
    # except:
    #     return "zz"


def getPosByVoice(turn, gameState):
    if (gameState == 0):
        return (1, 5)
    else:
        return (2, 5)