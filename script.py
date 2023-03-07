from pytube import Playlist
import os
from moviepy.editor import *
import shutil

url = input("Youtube playlist URL: ")
playlist = Playlist(url)

print('Number of videos in playlist: %s' % len(playlist.video_urls))


if not os.path.exists("tmp"):
	os.mkdir("tmp")

if not os.path.exists("audio"):
	os.mkdir("audio")

for video in playlist.videos:
	video.streams[0].download("tmp")
	
	

	li = video.streams[0].default_filename.rfind('.')

	fname = video.streams[0].default_filename[:li]

	video = VideoFileClip(os.path.join("tmp",video.streams[0].default_filename))
	video.audio.write_audiofile(os.path.join("audio",fname+".mp3"))


shutil.rmtree("tmp")