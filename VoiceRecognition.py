import pyaudio
from vosk import Model, KaldiRecognizer # For offline speech recogntion

# Language Model
model = Model("D:/SE/PBL2/LanguageModel/VoskModelSmallIndianEnglish")
recognizer = KaldiRecognizer(model, 16000)

def SpeechToText():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            break

    return text[14:-3].lower()

def getPosition():
    row = SpeechToText()
    print(row)
    col = SpeechToText()
    print(col)

    x = 0
    y = 0

    r = [
        ["a", "yeah", "eight", "ate"], # a
        ["b", "bee"], # b
        ["c", "see"], # c
        ["d", "the"], # d
        ["e"], # e
        ["f"], # f
        ["g", "je", "jee"], # g
        ["h"]  # h
    ]

    c = [
        ["one", "won", "van", "worn", "when", "wane"],  # 1
        ["two", "do", "too", "to"],  # 2
        ["three", "the", "threw", "tree", "free", "tea", "we"],  # 3
        ["four", "door", "ford"],  # 4
        ["five"],  # 5
        ["six"],  # 6
        ["seven", "even"],  # 7
        ["eight", "ate"]  # 8
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
        y+=1


    print(x)
    print(y)

    return (x, y)
