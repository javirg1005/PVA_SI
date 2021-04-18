import tkinter
import moviepy.editor as mp
import speech_recognition as sr
import os
import eel
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import tkinter
from tkinter.filedialog import askopenfilename
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

#'''

@eel.expose()
def abrir_archivo():
    print("Hola! Voy a abrir un archivo")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    tkinter._default_root.destroy()
    print(filename)
    chufla(filename)

@eel.expose()
def leerTextoBruto():
    f = open ('Transcripcion_Bruta.txt','r',encoding='utf8')
    texto = f.read()
    f.close()
    print(texto)
    eel.escribirTexto(texto)

@eel.expose()
def leerTextoRevisado():
    f = open ('Transcripcion_Revisada.txt','r',encoding='utf8')
    texto = f.read()
    f.close()
    eel.escribirTexto(texto)

def leerTextoRevisadoEtiquetar():
    f = open ('Transcripcion_Revisada.txt','r',encoding='utf8')
    texto = f.read()
    f.close()
    return texto

@eel.expose()
def leerTextoEtiquetado():
    f = open ('Transcripcion_Etiquetada.txt','r',encoding='utf8')
    texto = f.read()
    f.close()
    eel.escribirTexto(texto)

@eel.expose()
def guardarTextoRevisado(texto):
    f = open ('Transcripcion_Revisada.txt','w',encoding='utf8')
    f.write(texto)
    f.close()
    print(estemizar(limpiar(texto)))

#Hace hasta la transcripcion bruta
def chufla(path):
    texto = trocear_video(path)
    print("video troceado")
    escribir_transcripcion(texto, "Transcripcion_Bruta")

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

@eel.expose()
def etiquetar():
    # Diccionario de instrucciones
    # Violencia y extorsión de Patri
    instrucciones = {
        'arranc coch':'GO',
        'sub march':'GU',
        'aument march':'GU',
        'intermitent derech':'RB',
        'baj march':'GD',
        'dismin march':'GD',
        'intermitent izquierd':'LB',
        'fren':'BRK',
        'gir izquierd':'TL',
        'gir derech':'TR',
        'incorpor rotond':'RNDBT-IN',
        'entra rotond':'RNDBT-IN',
        'sal rotond':'RNDBT-OUT',
        'incorpor carreter':'ROAD-IN'
    }

    texto = leerTextoRevisadoEtiquetar()
    print(texto)
    txt_list = estemizar(limpiar(texto))
    print(txt_list)
    aux_list = []
    for inst, code in enumerate(txt_list):
        aux_list.append(code)
        if code in instrucciones:
            aux_list.append("<" + instrucciones[code] + ">")
        elif (len(txt_list) > inst + 1):
            code = txt_list[inst - 1] + " " + code
            if code in instrucciones:
                aux_list.append("<" + instrucciones[code] + ">")

    labeled_text = ' '.join(aux_list)
    print(labeled_text)
    escribir_transcripcion(labeled_text, "Transcripcion_Etiquetada")
    leerTextoEtiquetado()

def limpiar(text):
    sw = set(stopwords.words("spanish"))
    # Limpio con regex el texto
    text = re.sub('[%s]' % re.escape(string.punctuation + "'" + '"' + "’" + '”' + '“' + "•‘"), ' ', str(text))
    text = re.sub('\w*\d\w*', ' ', str(text))
    # Pongo el texto en minúsculas
    text = text.lower()
    # Tokenizo por palabras
    text = word_tokenize(str(text))
    tokens = []
    for t in text:
        if not t in sw:
            tokens.append(t)
    return tokens

def estemizar(token_list):
    new_token = []
    for token in token_list:
        token = SnowballStemmer('spanish').stem(token)
        new_token.append(token)
    return new_token

eel.init('web')
eel.start('index.html', mode='chrome-app')
