from pytube import YouTube
import os

ruta_descargas = os.path.expanduser("~") + "/Descargas"


def descargas_varias():
    archivo = "archivodetexto.txt"

    tamaño = os.path.getsize(archivo)
    
    if tamaño > 0:
        
        print("Iniciando descargas...")
        with open(archivo,"r") as archivo:
            
            for linea in archivo:
                video = YouTube(linea)
                print(f"Iniciando descarga : {video.title}")
                audio_stream = video.streams.filter(only_audio = True).first()
                audio_stream.download(output_path = ruta_descargas)
                print(f"Descarga completa : {video.title}")

    else:
        print("El archivo de texto esta vacio o no existe")
        exit()




def descarga_unica():
    url = input("ingrese la URL :")
    
    if url:
        video = YouTube(url)
        print(f"Iniciando descarga : {video.title}")
        
        audio = video.streams.filter(only_audio = True).first()
        audio.download(output_path = ruta_descargas)
        print(f"Descarga completa : {video.title}")

    else:
        print("Error: Campo vacio. Por favor añada algun enlace")
        return descarga_unica()

def como_usar():
    print("Como usar el programa :")
    print(" ")
    print("1:) Poder descargar varios archivos desde un archivo de texto. Abra el archivo de texto llamado 'archivodetexto' y añada las url de las musicas que desea descargar el programa se encargara de descargarlas 1 por 1.")
    print(" ")
    print("2:) Poder descargar solo 1 archivo. Solo pegue la URL de la musica y el programa se encargara de descargarla.")
    print(" ")
    print("3:) Para ver como se usa el programa.")
    print(" ")
    print("Importante la ruta por defecto de las descargas es 'Descargas' puedes cambiar la ruta editando el codigo.")
    print(" ")

def inicio():
    print("1 : Descargas varias.")
    print(" ")
    print("2 : Descarga unica.")
    print(" ")
    print("3 : Ayuda.")
    print(" ")
    print("4 : Salir.")

    opcion = str(input("elije alguna opcion 1/2/3/4 :"))


    if opcion == "1":
        descargas_varias()
    elif opcion == "2":
        descarga_unica()
    elif opcion == "3":
        como_usar()
    elif opcion == "4":
        exit()
    else:
        print("Error valor no valido")

while True:
    inicio()