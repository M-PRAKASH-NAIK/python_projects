from pytube import YouTube
link=input("Enter link to download  😎 :")
video=YouTube(link)
stream= video.streams.get_highest_resolution()
stream.download()
print(stream.download())
