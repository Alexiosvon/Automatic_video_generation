import os
import subprocess

# Set the path of input and output images.
PATH_IMAGE = "Image/image.jpg"
PATH_VIDEO = "Media/Demo_1080P.mp4"
VIDEO_TIME = "5"

# Check if the video file exists. If so, delete it.
if os.path.isfile(PATH_VIDEO) is True:
    os.remove(PATH_VIDEO)

# Set the command for processing the img2mp4.
cmd = "ffmpeg -ss 0 -t " + VIDEO_TIME +" -f lavfi -i color=c=0x000000:s=1920x1080:r=30  -i " + PATH_IMAGE + ' -filter_complex  "[1:v]scale=1920:1080[v1];[0:v][v1]overlay=0:0[outv]"  -map [outv] -c:v libx264 ' + PATH_VIDEO + " -y"

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
