import moviepy.editor as mp
import speech_recognition as sr
import os


#Conversion de Video a audio
video = mp.VideoFileClip('PVA_SI_Video.mp4') #Nombre del archivo
#audio= video.audio.write_audiofile(r'AudioV.wav') #Se escribe extra el codigo ha un archivo


#Reduccion de ruido
recibido_cambio = sr.Recognizer()
speech_audio = sr.AudioFile('AudioV.wav')

with speech_audio as fuente:
    recibido_cambio.adjust_for_ambient_noise(fuente)
    audio = recibido_cambio.record(fuente)

#Transcripcion
texto_transcrito = recibido_cambio.recognize_google(audio, language = "es-ES")
print(texto_transcrito)

# Guarda la transcripción en un archivo en la ruta actual
nombre_archivo_transcrito = os.path.splitext(respuesta)[0] + ".txt"
archivo_transcrito = open (nombre_archivo_transcrito,"w+")
archivo_transcrito.writelines(texto_transcrito)
archivo_transcrito.close()

print ("Se ha guardado la transcripción en el archivo " + nombre_archivo_transcrito + " en tu ruta actual")

#Reconocimiento
    
#Edicion

#Modificar e insertar

