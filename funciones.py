from ntpath import join
from sys import path
from typing import TextIO
from xml.dom.expatbuilder import TEXT_NODE
import os


def main():
    directorio_actual= os.getcwd()
    print(directorio_actual)
    directorio_textos = os.path.join(directorio_actual,"textos")
    print(directorio_textos)
    lista_archivos = os.listdir(directorio_textos)
    print(lista_archivos)
    print(lista_archivos[0])
    archivo_a_leer= os.path.join(directorio_textos,lista_archivos[0])
    print(archivo_a_leer)
    texto_libro = leer_archivo(archivo_a_leer)
    print(texto_libro[7000:8000])
    lista_palabras = texto_libro[6900:].split(" ")
    print(lista_palabras)
    

def leer_archivo(nombre_archivo:str) -> str:
    
    # lee un archivo. Revibe " nombre_archivo" y regresa una cadena de Texto 
    
    with open (nombre_archivo, 'r', encoding="utf-8") as archivo:
        texto = archivo.read()
    return texto

def limpia_texto(texto) -> str:
     cadena= "\n.,-_" 
     texto_limpio = texto.replace(cadena)
    
if __name__ == "__main__":
    main()
