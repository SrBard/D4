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
    texto_limpio=limpiar_texto(texto_libro)
    lista_palabras = texto_libro[6900:].split(" ")
    print(lista_palabras)
    listas_palabras_limpias=texto_libro[0:100]
    
    

def leer_archivo(nombre_archivo:str) -> str:
    
    # lee un archivo. Revibe " nombre_archivo" y regresa una cadena de Texto 
    
    with open (nombre_archivo, 'r', encoding="utf-8") as archivo:
        texto = archivo.read()
    return texto

def limpiar_texto(texto) -> str:
     cadena= "\n.,-_" 
     for simbolo in cadena:
         texto = texto.replace(simbolo," ")
         return texto

def limpiar_lista_palabras(lista) ->list:
     cadena = "\n.,-_"
     nueva_lista=[]
     lista_nuevecita=[] 
     for palabra in cadena:
         for simbolo in cadena:
             palabra = palabra.replace(simbolo," ")
         nueva_lista.append(palabra)  
     for palabra in nueva_lista:
         if " " in palabra:
             nuevas_palabras = palabra.split()
             lista_nuevecita.extend(nuevas_palabras)
             nueva_lista.remove(palabra)
     nueva_lista.extend(lista_nuevecita)       
     return nueva_lista     

if __name__ == "__main__":
    main()
