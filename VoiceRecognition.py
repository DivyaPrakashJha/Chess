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

    print("1" + text)
    while True:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text1 = recognizer.Result()
            break
    print("2" + text1)
    return (text[14:-3].lower(), text1[14:-3].lower())

def getPosition():
    (row, col) = SpeechToText()

    print(row)
    print(col)

    x = 0
    y = 0

    r = [
        ["a", "yeah", "ate","eh","they","hey","a."], # a
        ["b", "bee","b."], # b
        ["c", "see","c."], # c
        ["d", "the","d.","day"], # d
        ["e","e."], # e
        ["f","f."], # f
        ["g", "je", "jee","g."], # g
        ["h","edge","eight","it","h.","it's"]  # h
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
        y+=1


    print(x)
    print(y)

    return (y, x)
