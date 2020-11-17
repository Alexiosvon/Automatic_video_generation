import os
import wave
import math
import subprocess
from pydub import AudioSegment

# MP3、WAV、JPG的地址
PATH_MP3 = 'Media/MP3/'
PATH_WAV = 'Media/WAV/'
PATH_IMAGE = "Image/"
PATH_VIDEO = "Media/MP4/"
PATH_VIDEO_A = "Media/MP4_A/"


# MP3转WAV函数
def MP32WAV(mp3_path, wav_path):
    MP3_File = AudioSegment.from_mp3(file=mp3_path)
    MP3_File.export(wav_path, format="wav")


# 批量读入MP3音频,并批量转换为WAV
# 得到MP3文件的相对地址
paths = os.listdir(PATH_MP3)
MP3_PATHS = []
for MP3_PATH in paths:
    MP3_PATHS.append(PATH_MP3 + MP3_PATH)
# print(MP3_PATHS)

# 得到MP3文件对应的WAV文件的相对地址
WAV_PATHS = []
for MP3_PATH in MP3_PATHS:
    WAV_PATH = PATH_WAV + MP3_PATH[1:].split('.')[0].split('/')[-1] + '.wav'
    WAV_PATHS.append(WAV_PATH)
# print(WAV_PATHS)

# 将MP3文件转化成WAV文件，若已转换，删除源文件重新转换
for WAV_PATH in WAV_PATHS:
    if os.path.isfile(WAV_PATH) is True:
        os.remove(WAV_PATH)
for (MP3_PATH, WAV_PATH) in zip(MP3_PATHS, WAV_PATHS):
    MP32WAV(MP3_PATH, WAV_PATH)

# 读取WAV文件对应时长
TIMES = []
for WAV_PATH in WAV_PATHS:
    fr = wave.open(WAV_PATH, 'rb')
    time = math.floor(fr.getnframes() / fr.getframerate())
    TIME = str(time)
    TIMES.append(TIME)
# print(TIMES)

# 对音频文件配图
# 读取图片相对地址
paths = os.listdir(PATH_IMAGE)
IMAGE_PATHS = []
for IMAGE_PATH in paths:
    IMAGE_PATHS.append(PATH_IMAGE + IMAGE_PATH)
# print(IMAGE_PATHS)

# 得到WAv文件对应视频相对地址
VIDEO_PATHS = []
for WAV_PATH in WAV_PATHS:
    VIDEO_PATH = PATH_VIDEO + WAV_PATH[1:].split('.')[0].split('/')[-1] + '.mp4'
    VIDEO_PATHS.append(VIDEO_PATH)
# print(VIDEO_PATHS)

# 将WAV文件转化成MP4文件，若已转换，删除源文件重新转换
for VIDEO_PATH in VIDEO_PATHS:
    if os.path.isfile(VIDEO_PATH) is True:
        os.remove(VIDEO_PATH)
for (VIDEO_PATH, IMAGE_PATH, TIME) in zip(VIDEO_PATHS, IMAGE_PATHS, TIMES):
    cmd = "ffmpeg -ss 0 -t " + TIME + " -f lavfi -i color=c=0x000000:s=1920x1080:r=30  -i " + IMAGE_PATH + ' -filter_complex  "[1:v]scale=1920:1080[v1];[0:v][v1]overlay=0:0[outv]"  -map [outv] -c:v libx264 ' + VIDEO_PATH + " -y"
    subprocess.call(cmd, shell=True)

# 得到MP4文件对应的MP4_S文件相对地址
VIDEO_PATH_AS = []
for VIDEO_PATH in VIDEO_PATHS:
    VIDEO_PATH_A = PATH_VIDEO_A + VIDEO_PATH[1:].split('.')[0].split('/')[-1] + '.mp4'
    VIDEO_PATH_AS.append(VIDEO_PATH_A)
# print(VIDEO_PATH_AS)

# 对MP4文件配音，若已存在，删除源文件重新转换
for VIDEO_PATH_A in VIDEO_PATH_AS:
    if os.path.isfile(VIDEO_PATH_A) is True:
        os.remove(VIDEO_PATH_A)
for (VIDEO_PATH, WAV_PATH, VIDEO_PATH_A) in zip(VIDEO_PATHS, WAV_PATHS, VIDEO_PATH_AS):
    cmd = "ffmpeg -i " + VIDEO_PATH + " -i " + WAV_PATH + " -c:v copy -c:a aac -strict experimental " + VIDEO_PATH_A
    subprocess.call(cmd, shell=True)
