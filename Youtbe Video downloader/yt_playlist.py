import pytube

from pytube import Playlist

py = Playlist("https://youtube.com/playlist?list=PLttcEXjN1UcHu4tCUSNhhuQ4riGARGeap")

print(f'Dowinling : {py.title}')

for video in py.videos:
    video.streams.first().download()