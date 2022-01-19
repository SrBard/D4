from ntpath import join
from sys import path
from typing import TextIO
from xml.dom.expatbuilder import TEXT_NODE
import os

directorio_actual= os.getcwd()
print(directorio_actual)
directorio_textos = os.path.join(directorio_actual,"textos")
lista_archivos = os.listdir(directorio_textos)
print(lista_archivos)
archivo_a_leer= os.path.join(directorio_textos,lista_archivos[0])
texto_libro = leer_archivo(lista_archivos[0])
print(texto_libro[0:200])

def leer_archivo(nombre_archivo:str) -> str:
    
    # lee un archivo. Revibe " nombre_archivo" y regresa una cadena de Texto 
    
    with open (nombre_archivo,'r') as archivo:
        texto = archivo.read()
    return texto
    
    
if __name__ == "__main__":
    main()
