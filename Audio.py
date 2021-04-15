import moviepy.editor as mp
import speech_recognition as sr
import os
import eel 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip

'''
eel.init('web')
eel.start('index.html')
'''

def chufla(path):
    texto = trocear_videoV2(path)
    print("video troceado")
    '''
    texto = ""
    
    onlyfiles = next(os.walk("\\SVideo"))[2] #dir is your directory path as string
    n_files = len(onlyfiles)
    
    for i in range(n_files):
        video = mp.VideoFileClip(".\\SVideo\\" + i +".mp4")      
        texto = texto + tratamiento_video(video)
    #se edita'''
    
    #se etiqueta

    #se imprime en un txt
    escribir_transcripcion(texto)



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

def trocear_videoV2(path):
    required_video_file = mp.VideoFileClip(path)
    chunk_dur_ini = 0
    chunk_dur_fin = 60
    texto = ''
    duracion = int(required_video_file.duration) #Duracion del video
    while (duracion > chunk_dur_ini):
        starttime = chunk_dur_ini
        endtime = chunk_dur_fin
        with VideoFileClip(path) as video:
            #new = video.subclip(starttime, endtime)
            new = ffmpeg_extract_subclip(path, starttime, endtime, targetname = "D:\Github\PVA_SI\PruebasSplit\Meh.mp4")
            texto = texto + tratamiento_video(new)
        chunk_dur_ini = chunk_dur_ini + 60
        chunk_dur_fin = chunk_dur_fin + 60
    return texto
    
def tratamiento_video(video):
    audio= video.audio.write_audiofile(r'AudioV.wav')
    recibido_cambio = sr.Recognizer()
    speech_audio = sr.AudioFile('AudioV.wav')

    with speech_audio as fuente:
        #Se reduce el ruido
        recibido_cambio.adjust_for_ambient_noise(fuente)
        audio = recibido_cambio.record(fuente)
        #Transcripcion
        texto_transcrito = recibido_cambio.recognize_google(audio, language = "es-ES")
        print(texto_transcrito)
        return texto_transcrito

def escribir_transcripcion(lista):
    nombre_archivo_transcrito = os.path.splitext("Transcripcion")[0] + ".txt"
    archivo_transcrito = open (nombre_archivo_transcrito,"w+")
    archivo_transcrito.writelines(lista)
    archivo_transcrito.close()
    print ("Se ha guardado la transcripción en el archivo " + nombre_archivo_transcrito + " en tu ruta actual") 

chufla('PruebasSplit\VideoTest.mp4')
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