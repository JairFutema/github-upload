from pytube import YouTube
print("Descargar videos de youtube")
link = input("ingrese la url del video a descargar")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download(output_path='C:/video')
print("Video descargado con exito")

