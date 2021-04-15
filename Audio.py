import moviepy.editor as mp
import speech_recognition as sr
import os
import eel 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

eel.init('web')
eel.start('index.html')


def main(path):
    trocear_video(path)
    print("video troceado")
    texto = ""
    '''
    while True: ##Trabajando en como hacer el bucle y la i
        video = mp.VideoFileClip(".\\SVideo\\" + i +".mp4")
        tratamiento_video(video, i)
        texto = texto + tratamiento_video
    #se edita
    
    #se etiqueta

    #se imprime en un txt
    escribir_transcripcion(texto)
'''




#Se corta el video en segmentos mas pequeños para poder tratarlos
def trocear_video(path):
    required_video_file = mp.VideoFileClip(path)
    chunk_dur_ini = 0
    chunk_dur_fin = 60
    i = 0
    duracion = int(required_video_file.duration) #Duracion del video
    while (duracion > chunk_dur_ini):
        starttime = chunk_dur_ini
        endtime = chunk_dur_fin
        ffmpeg_extract_subclip(path, starttime, endtime, targetname= ".\SVideo\\" + str(i) + ".mp4")
        i = i + 1
        chunk_dur_ini = chunk_dur_ini + 60
        chunk_dur_fin = chunk_dur_fin + 60
    
def tratamiento_video(video, i):
    audioVideo = video.audio.write_audiofile(i+'.wav') #Se escribe extra el codigo ha un archivo
    #Se reduce el ruido
    recibido_cambio = sr.Recognizer()
    speech_audio = sr.AudioFile('AudioV.wav')
    speech_audio = sr.AudioFile(audioVideo)

    speech_audio = speech_audio

    with speech_audio as fuente:
        recibido_cambio.adjust_for_ambient_noise(fuente)
        audio = recibido_cambio.record(fuente)
        #Transcripcion
        texto_transcrito = recibido_cambio.recognize_google(audio, language = "es-ES")
        return texto_transcrito

def escribir_transcripcion(lista):
    nombre_archivo_transcrito = os.path.splitext("Transcripcion")[0] + ".txt"
    archivo_transcrito = open (nombre_archivo_transcrito,"w+")
    archivo_transcrito.writelines(lista)
    archivo_transcrito.close()
    print ("Se ha guardado la transcripción en el archivo " + nombre_archivo_transcrito + " en tu ruta actual") 

#Reconocimiento
    
#Edicion

#Modificar e insertar

'''
video = mp.VideoFileClip('PVA_SI_Video.mp4') #Nombre del archivo

#Conversion de Video a audio
video = mp.VideoFileClip('PVA_SI_Video.mp4') #Nombre del archivo
duracion = int(video.duration) #Duracion del video

#Se corta el video en chunks


#TODO cambiar esto a que cada chunk de audio
audio= video.audio.write_audiofile(r'AudioV.wav') #Se escribe extra el codigo ha un archivo


#Reduccion de ruido
recibido_cambio = sr.Recognizer()
speech_audio = sr.AudioFile('AudioV.wav')

speech_audio = speech_audio.

with speech_audio as fuente:
    recibido_cambio.adjust_for_ambient_noise(fuente)
    audio = recibido_cambio.record(fuente)

    #Transcripcion
    texto_transcrito = recibido_cambio.recognize_google(audio, language = "es-ES")
    print(texto_transcrito)

# Guarda la transcripción en un archivo en la ruta actual
nombre_archivo_transcrito = os.path.splitext("Transcripcion")[0] + ".txt"
archivo_transcrito = open (nombre_archivo_transcrito,"w+")
archivo_transcrito.writelines(texto_transcrito)
archivo_transcrito.close()

print ("Se ha guardado la transcripción en el archivo " + nombre_archivo_transcrito + " en tu ruta actual")

#Reconocimiento
    
#Edicion

#Modificar e insertar

'''