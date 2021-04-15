#!/usr/bin/env python

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp

# Replace the filename below.
#required_video_file = mp.VideoFileClip('.\PVA_SI_Video.mp4')
print("Pilla el path")
path = "D:\Github\PVA_SI\PruebasSplit\PVA_SI_Video.mp4"
required_video_file = mp.VideoFileClip("D:\Github\PVA_SI\PruebasSplit\PVA_SI_Video.mp4")
# ['0-60', '60-120']

chunk_dur_ini = 0
chunk_dur_fin = 60
i = 0
print("Calcula la duracion")
duracion = int(required_video_file.duration) #Duracion del video
print("Duración:", duracion)
print("Va a entrar en el bucle")
while (duracion > chunk_dur_ini):
  print("Estoy dentro")
  starttime = chunk_dur_ini
  endtime = chunk_dur_fin
  ffmpeg_extract_subclip(path, starttime, endtime, targetname= "D:\Github\PVA_SI\PruebasSplit\\" + str(i) + ".mp4")
  i = i + 1
  chunk_dur_ini = chunk_dur_ini + 60
  chunk_dur_fin = chunk_dur_fin + 60
  print("Duración inicial del segmento", i, "->", chunk_dur_ini)
  print("Duración final del segmento", i, "->", chunk_dur_fin)

'''
for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mp4")
  '''