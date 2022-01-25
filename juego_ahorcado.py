import ahorcado
import random
import funciones
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
    print("leyendp archivo: ",archivo_a_leer)
    
    texto_libro = funciones.leer_archivo(archivo_a_leer)
    print(len(texto_libro))
    lista_palabras_sucias = texto_libro[6949:].split(" ")
    lista = []
    for palabra in lista_palabras_sucias:
        if palabra != ' ':
            lista.append(palabra)
    print("===========")
    print(lista[0:100])
    listas_palabras_limpias = funciones.limpiar_lista_palabras(lista_palabras_sucias)
    juego=True
    ganados = 0
    juegos_perdidos = 0
    while juego== True:
        palabra = random.choice(listas_palabras_limpias)
        gano = ahorcado.ahorcado(palabra,6)
        if gano ==True:
            ganados +=1
        juegos_perdidos += 1
        print("juego ganados: ", ganados," perdidos: ",juegos_perdidos)    
        opcion = input("¿Quieres jugar otra vez (S/N): ")
        if len(opcion)>0:
            opcion = opcion.upper()
            if opcion[0] == "N":
                juego = False
    

if __name__ == "__main__":
    main()
