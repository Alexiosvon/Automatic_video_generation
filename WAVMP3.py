from pydub import AudioSegment


# mp3 to wav
def MP32WAV(mp3_path, wav_path):
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File.export(wav_path, format="wav")


# wav to mp3
def WAV2MP3(wav_path, mp3_path):
    WAV_File = AudioSegment.from_wav(file=wav_path)
    WAV_File.export(mp3_path, format="mp3")


MP3_PATH = 'Media/Demo.mp3'
WAV_PATH = 'Media/Demo.wav'

if os.path.isfile(MP3_PATH) is True:
    os.remove(MP3_PATH)
WAV2MP3(WAV_PATH, MP3_PATH)

if os.path.isfile(WAV_PATH) is True:
    os.remove(WAV_PATH)
MP32WAV(MP3_PATH, WAV_PATH)
