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
    # col = text[1]
    # row = text[0]

    print(row)
    print(col)
    return (1, 0)
