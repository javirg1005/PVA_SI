import tkinter
import moviepy.editor as mp
import speech_recognition as sr
import os
import eel
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import tkinter
from tkinter.filedialog import askopenfilename


#'''

@eel.expose()
def abrir_archivo():
    print("Hola! Voy a abrir un archivo")
    #Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    #tkinter._support_default_root = False
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    tkinter._default_root.destroy()
    print(filename)
    eel.showAnswers(filename)
    chufla(filename)

@eel.expose()
def leerTextoBruto():
    f = open ('Transcripcion_Bruta' + '.txt','rb')
    f.close()
    return f

#Hace hasta la transcripcion bruta
def chufla(path):
    texto = trocear_video(path)
    print("video troceado")
    escribir_transcripcion(texto, "Transcripcion_Bruta")
    return texto
    #Revision de usuario
    
    #se imprime en un txt
    #escribir_transcripcion(texto, "Transcripcion_Revisada")
    

#Se corta el video en segmentos mas pequeños para poder tratarlos
def trocear_video(path):
    required_video_file = mp.VideoFileClip(path)
    chunk_dur_ini = 0
    chunk_dur_fin = 60
    texto = ''
    duracion = int(required_video_file.duration) #Duracion del video
    while (duracion > chunk_dur_ini):
        starttime = chunk_dur_ini
        endtime = chunk_dur_fin
        with VideoFileClip(path) as video:
            new = ffmpeg_extract_subclip(path, starttime, endtime, targetname = ".\Segmentos\Meh.mp4")
            texto = texto + tratamiento_audio(".\Segmentos\Meh.mp4")
        chunk_dur_ini = chunk_dur_ini + 60
        chunk_dur_fin = chunk_dur_fin + 60
    return texto
    
def tratamiento_audio(path): # se recibe un archivo .wav
    video = mp.VideoFileClip(path)
    audio = video.audio.write_audiofile(r'AudioV.wav') # de cuando se recibia un vídeo
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

def escribir_transcripcion(lista, name):
    nombre_archivo_transcrito = os.path.splitext(name)[0] + ".txt"
    archivo_transcrito = open(nombre_archivo_transcrito,"w+", encoding="utf-8")
    archivo_transcrito.writelines(lista)
    archivo_transcrito.close()
    print ("Se ha guardado la transcripción en el archivo " + nombre_archivo_transcrito + " en tu ruta actual")
#Testing
#chufla('PruebasSplit\Video_Coche.mp4')
#Reconocimiento
    
#Edicion

#Modificar e insertar

eel.init('web')
eel.start('index.html', mode='chrome-app')
