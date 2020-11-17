import wave
import math

WAV_PATH = "Media/Demo.wav"

fr = wave.open(WAV_PATH, 'rb')
time = math.ceil(fr.getnframes() / fr.getframerate())

print(time)