import pyaudio
from vosk import Model, KaldiRecognizer # For offline speech recogntion
import time

# Language Model
model = Model("D:/SE/PBL2/LanguageModel/VoskModelSmallIndianEnglish")
recognizer = KaldiRecognizer(model, 16000)

def SpeechToText():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    duration = 3
    startTime = time.time()

    while True:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            break

        if time.time() - startTime > duration:
            return ""
            break

    return text[14:-3].lower()

def getPosition():
    row = ""
    while not len(row):
        row = SpeechToText()
    print(row)
    col = ""
    while not len(col):
        col = SpeechToText()
    print(col)

    x = 0
    y = 7

    r = [
        ["a", "yeah", "ate","eh","they","hey", "eight"], # a
        ["b", "bee"], # b
        ["c", "see"], # c
        ["d", "the", "day"], # d
        ["e", "yeah", "he"], # e
        ["f"], # f
        ["g", "je", "jee"], # g
        ["h","edge", "it","it's"]  # h
    ]

    c = [
        ["one", "won", "van", "worn", "when", "wane"],  # 1
        ["two", "do", "too", "to"],  # 2
        ["three", "the", "threw", "tree", "free", "tea", "we"],  # 3
        ["four", "door", "ford","source"],  # 4
        ["five","why","while"],  # 5
        ["six","sec"],  # 6
        ["seven", "even"],  # 7
        ["eight", "ate","it"]  # 8
    ]

    flag = 0
    for li in r:
        for element in li:
            if (element == row):
                flag = 1

        if (flag):
            break;
        x+=1

    flag = 0
    for li in c:
        for element in li:
            if (element == col):
                flag = 1
        if (flag):
            break
        y-=1

    if x == 8:
        x = ord(row[0]) - ord('a')
    y = max(y, 0)

    print(x)
    print(y)

    return (x, y)
