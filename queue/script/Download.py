from pytube import YouTube

def Download(link):
    try:
        yt = YouTube(link)
    except:
        return
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download()
    return