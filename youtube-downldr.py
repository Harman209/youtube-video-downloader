from pytube import YouTube

url = input('Pls Insert the url of the video: ')

video = YouTube(url)

print(video.title)

video = video.streams.get_highest_resolution()

video.download()
