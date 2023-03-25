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
            print(text)
            break;

    return text.lower()
def getPosition(text):
    if (text == "be one" or "b1"):
        return (())
