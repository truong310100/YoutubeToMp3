import os, re
import moviepy.editor as mp
from pytube import YouTube, Playlist

def Download_Video_Mp3(videoMP3_url):
    download_folder = "./Downloads"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    try:
        yt = YouTube(videoMP3_url)
        streams = yt.streams.filter(only_audio=True).first()
        filename = f"{yt.title}.mp3"
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
            mp3_path = os.path.join(download_folder, os.path.splitext(file)[0] + ".mp3")
            # print("Converting:", file)
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            # print("Converted:", file)
            os.remove(mp4_path)
            # print('Removed:', mp4_path)

def check_link():
    check = input(" By Nguyen Lam Truong\n >> Input your link Youtube: ")
    if "watch?v=" in check:
        Download_Video_Mp3(check)
    elif "playlist?list=" in check:
        Download_Playlist_Mp3(check)
    else:
        print("ERROR")

check_link()
os.system("start Downloads & pause & exit")
# by Nguyen Lam Truong
# v26.07.2023 19:50