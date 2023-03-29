import pytube
from pytube.cli import on_progress

#File Path
FILE_PATH = "C:\\Users\\PATH\\TO\\FOLDER"

#Audio downloader function
def audioDownloader(url):
    try:
        youtube = pytube.YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.get_audio_only()
        print("Starting Audio Download... \n")
        video.download(FILE_PATH, filename_prefix = "(AUDIO) - ")
        print("Audio Done")
    except:
        print("Error")

#Video downloader function
def videoDownloader(url):
    try:
        youtube = pytube.YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.get_highest_resolution()
        print("Starting Video Download... \n")
        video.download(FILE_PATH, filename_prefix = "(VIDEO) - ")
        print("Video Done")
    except:
        print("Error")

#Main function
def main():
    choice = input("Download format: Video, Audio or Both? (V/A/B) \n")
    url = input("URL: ")

    if choice.upper() == 'A':
        audioDownloader(url)
    elif choice.upper() == 'V':
        videoDownloader(url)
    elif choice.upper() == 'B':
        audioDownloader(url)
        videoDownloader(url)
    else:
        print("Invalid Choice")

#Calling Main function
if __name__ == "__main__":
    main()