import os, platform
from pytube import YouTube
import time

if platform.system() == "Linux":
    os.system("pip install pytube & clear")
elif platform.system() == "Windows":
    os.system("pip install pytube & cls & title Youtube Downloader")
else:
    os.system("pip install pytube & clear")

ss = input("Enter YT Link : ")

yt = YouTube(ss)
ys = yt.streams.get_highest_resolution()
ys.download()
print("Successfuly Download!")
time.sleep(2)
