import tkinter as tk
from tkinter import *
import subprocess
import threading
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from tkinter import messagebox

# sample== https://www.youtube.com/watch?v=ZHQaA9Z6vlQ
download_folder = "C:\\Users\\Harshit\\Downloads"
fileSizeInBytes = 0
MaxFileSize = 0

# decicde the link is a playlist or video and call the function accordingly
def VideoOrPlaylist():
    global download_folder 
    download_folder = filedialog.askdirectory()
    folder_path_label.config(text=' Download Location: {}'.format(download_folder))

    # Create a new thread that will run the download operation
    download_thread = threading.Thread(target=DownloadOperation)

    # Start the new thread
    download_thread.start()

def DownloadOperation():
    # Check if the link is a playlist or a video and call the appropriate function
    if "playlist" in youtubeEntry.get():
        DownloadPlaylist()
    else:
        DownloadFile()

def DownloadFile():
        global MaxFileSize,fileSizeInBytes,download_folder
        choice = youtubeChoices.get()
        video = youtubeEntry.get()

        if(len(video)>1):
            youtubeEntryError.config(text="")
            print(video,"at",download_folder)
            yt = YouTube(video,on_progress_callback=progress_function)
            #on_complete_callback=complete
            print("Video Name is:\n\n",yt.title)
            
            
            if(choice == downloadChoices[0]):
                print("720p Video file downloading...")
                loadingLabel.config(text="720p Video file downloading...")#
                
                selectedVideo =yt.streams.filter(progressive=True).first()
                            
            elif(choice == downloadChoices[1]):
                print("144p video file downloading...")
                selectedVideo =yt.streams.filter(progressive=True,
                                                 file_extension='mp4').last()
              
            elif(choice == downloadChoices[2]):
                print("3gp file downloading...")
                selectedVideo =yt.streams.filter(file_extension='3gp').first()
                
            elif(choice == downloadChoices[3]):
                print("Audio file downloading...")
                selectedVideo = yt.streams.filter(only_audio=True).first()
                
            fileSizeInBytes = selectedVideo.filesize
            MaxFileSize = fileSizeInBytes/1024000
            MB = str(MaxFileSize) + " MB"
            print("File Size = {:00.00f} MB".format(MaxFileSize))
            
            #now Download ------->
            selectedVideo.download(download_folder)               
            #==========>
            complete(download_folder)
            
        else:
            youtubeEntryError.config(text="Please paste youtube video/playlist link",
                                         fg="red")

def DownloadPlaylist():
    global download_folder
    quality = youtubeChoices.get()  
    playlist_url = youtubeEntry.get()

    if not playlist_url or not download_folder or not quality:
        messagebox.showerror('Error', 'Please provide a playlist URL, select a download folder, and select a quality')
        return

    playlist = Playlist(playlist_url)
    total_videos = len(playlist.video_urls)
    current_video = 0
    for url in playlist.video_urls:
        current_video += 1
        loadingLabel.config(text=f"Downloading video {current_video} of {total_videos}")
        video = YouTube(url, on_progress_callback=progress_function)
        stream = video.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()
        if stream is None:
            print(f"No matching stream found for video {video.title}, downloading highest available quality instead")
            stream = video.streams.get_highest_resolution()
        if stream is not None:
            stream.download(download_folder)
        else:
            print(f"No streams found for video {video.title}")

    # open the folder after download
    subprocess.Popen(f'explorer {download_folder}')

#============progress bar==================
def progress_function(stream, chunk, bytes_remaining):
    if fileSizeInBytes is not None and bytes_remaining is not None:
        current = (stream.filesize - bytes_remaining)
        percent = (current / stream.filesize) * 100
        print("{:00.0f}% downloaded".format(percent))
        progress_var.set(percent)  # Update the progress_var
        root.update_idletasks()
    else :
        messagebox.showerror('Error', 'Unable to get file size or remaining bytes')

def complete(download_folder):
    print("Download completed")
    loadingLabel.config(text="Download completed")
    messagebox.showinfo('Success', 'Download completed successfully')
    folder = download_folder.replace('/', '\\')  # Replace forward slashes with backslashes
    subprocess.Popen(f'explorer "{folder}"')  # Wrap the path in quotes  

#================tkinter window       
root = Tk()
root.title("Youtube Video downloader - Harshit khandelwal")
#===============contents strech ac to windows strech====      
root.grid_columnconfigure(0, weight=1)  #strech things Horiontally

#=============youtube link label=================
youtubeLinkLabel = Label(root,
                        text="Please paste the youtube link here: ",
                                      fg="blue",font=("Agency FB", 30))
youtubeLinkLabel.grid()
#==========get youtube link in entry box
youtubeEntryVar = StringVar()
youtubeEntry = Entry(root, width=50,
                         textvariable=youtubeEntryVar)
youtubeEntry.grid(pady=(0))

#=========when link is wrong print this label
youtubeEntryError = Label(root,fg="red",
                        text="",font=("Agency FB", 20))
youtubeEntryError.grid()

# Entry label if user don`t choose directory
fileLocationLabelError = Label(root,
                                            text="", font=("Agency FB", 20))
fileLocationLabelError.grid()

folder_path_label = Label(root, text="Download Location: {}".format(download_folder),
                            font=("Agency FB", 20),fg="blue",wraplength=500,justify="center")

folder_path_label.grid()

#======= what to download choice==========
youtubeChooseLabel = Label(root,
                            text="Please choose what to download: ",
                                            font=("Agency FB", 20))
youtubeChooseLabel.grid()

# Combobox with four choices:
downloadChoices = [
    #  "MP4_1080p",
                   "MP4_720p",
                   "Mp4_144p",
                   "Video_3gp",
                   "Song_MP3"]

youtubeChoices = ttk.Combobox(root,values=downloadChoices)
youtubeChoices.grid()
             
#==================Download button===================
downloadButton = Button(root,
                                     text="Download", width=15,bg="green",
                                     command=VideoOrPlaylist,)
downloadButton.grid(pady=(20,20))

# Progressbar ======
progress_var = tk.DoubleVar()  # Use DoubleVar to support floating point values
progress_bar = ttk.Progressbar(root, length=200, mode='determinate', variable=progress_var, maximum=100)  # Set maximum to 100
progress_bar.grid(pady=(20,20))

#==================
loadingLabel = ttk.Label(root,text="App developed by >> Harshit Khandelwal",
                                font=("Agency FB", 20))
loadingLabel.grid()

root.mainloop()
