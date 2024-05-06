import os
import re
import moviepy.editor as mp
from pytube import YouTube, Playlist

def clean_filename(filename):
    return re.sub(r'[\\/:"*?<>|]+', '', filename)

def Download_Video_Mp3(videoMP3_url):
    download_folder = "./Downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    try:
        yt = YouTube(videoMP3_url)
        streams = yt.streams.filter(only_audio=True).first()
        filename = clean_filename(yt.title) + ".mp3"
        streams.download(download_folder, filename=filename)
        print("Downloaded {}".format(filename))
    except Exception as e:
        print(f"Error: {e}")

def Download_Playlist_Mp3(playlistMP3_url):
    download_folder = "./Downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    playlist = Playlist(playlistMP3_url)
    for url in playlist:
        print("______________________________________________________________________________________")
        print("Downloading:", url)
        file = YouTube(url).streams.filter(only_audio=True).first().download(download_folder)
        print("Downloaded:", url)
        if re.search("mp4", file):
            mp4_path = os.path.join(download_folder, file)
            mp3_path = os.path.join(download_folder, clean_filename(os.path.splitext(file)[0]) + ".mp3")
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

def check_link():
    check = input("\n >> Input your link Youtube: ")
    if "watch?v=" in check:
        Download_Video_Mp3(check)
    elif "playlist?list=" in check:
        Download_Playlist_Mp3(check)
    else:
        print("ERROR")

check_link()
os.system("start Downloads & pause & exit")

# by Nguyen Lam Truong
# v06.05.2024 13:25