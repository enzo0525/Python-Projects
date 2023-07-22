from pytube import YouTube
from tqdm import tqdm
import os
import time

def video_download(yt, download_path):
    yt.streams.get_highest_resolution().download(output_path=PATHS[download_path])
    for i in tqdm(range(100)):
        time.sleep(0.1)
    print('Video succesfully downloaded in', download_path)

def audio_download(yt, download_path):
    video = yt.streams.filter(abr='128kbps').first()
    out_file = video.download(output_path=PATHS[download_path])
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    for i in tqdm(range(100)):
        time.sleep(0.1)
    print('Audio succesfully downloaded in', download_path)

USERNAME_PC = os.environ.get('USERNAME')
PATHS = {'desktop':f'/Users/{USERNAME_PC}/Desktop/', 'music':f'/Users/{USERNAME_PC}/Music/', 'videos':f'/Users/{USERNAME_PC}/Videos/'}

def main():
    while True:
        download_path = input('What folder would you like to your file be stored in? (Desktop/Videos/Music) \n')
        if download_path in PATHS:
            break
    while True:
        try:
            url = input('URL:')
            yt = YouTube(url)
            break
        except:
            print('Invalid url, try again.')
            continue

    while True:
        file_type = input('Would you like to be a Video or Audio? (V/A) \n')
        if file_type.lower() == 'v':
            video_download(yt, download_path)
            break
        elif file_type.lower() == 'a':
            audio_download(yt, download_path)
            break
        else:
            continue
    input("Press enter to close the terminal.")

if __name__ == '__main__':
    main()