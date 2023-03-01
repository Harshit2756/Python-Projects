from pytube import YouTube

#/progress bar code
def progress_bar(progress,total):
    percent = 100*(progress/float(total))
    bar ='█' * int(percent) + '-' * (100 - int(percent))
    print (f"\r |{bar}| {percent:.2f}%", end="\r")

#/Taking the Url
URL = input('Enter a video URL:')

youtube_1=YouTube(URL)

#/To get the title of the video
print("\n\t\t Title : " + youtube_1.title + "\n\n=======================================================================================================")

#/To get the T of the video
print("\n\t\t Thumbnail : "+youtube_1.thumbnail_url+"\n\n=======================================================================================================")

#/Format of the file
fileType =int(input("\n\t\t Select filetype \n\t 1.Video \n\t 2.Audio \n\t"))

print("\n=======================================================================================================")

#/find the file format acc to the user input
if fileType==1:
    files = youtube_1.streams.filter(mime_type="video/mp4",progressive=True)
else:
    files = youtube_1.streams.filter(only_audio=True)

print('\n\t\t Select the the Quality: \n\t\t')

#/stores the list of the of the selected file type and then print 
vid = list(enumerate(files))
for i in vid:
    print(i)

print("\n")
strm = int (input())

print("\n=======================================================================================================")

#/download the video in the selected filetype and quality.
files[strm].download()

print('successfully downloaded 🥳🥳')

