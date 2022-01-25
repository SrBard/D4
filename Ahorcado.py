from operator import truediv
from pickle import TRUE
import funciones

def ahorcado(palabra_oculta, num_strikes_max):
    num_strikes = 0
    ganado = False
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #lista_abcdario = []
    #for letra in abc:
    #    lista_abcdario.append(letra)
    lista_abcdario = [letra for letra in abc]
    lista_letras = crear_lista_letras(palabra_oculta)
    lista_letras[1] = ['A',True]
    print(lista_letras)
    while num_strikes<num_strikes_max or ganado == False :
        mostrar_palabra(lista_letras)
        mostrar_abcdario(lista_abcdario)
        break
        #mostrar_strikes()
        # palabra = input("Si adivinaste la palabra, ingrésala, o escoge una letra:")
        # if palabra == palabra_oculta:
        #     ganado = True
        #     #rellenar letras y mostrar_palabra()
        # else:
        #     #checar la longitud
        #     if len(palabra) > 0:
        #         letra = palabra[0]
        #         #checar si la letra está en la palabra
        #     else:
        #         print("Es necesario ingresar una palabra o una letra...")

def mostrar_abcdario(lista):
    for letra in lista:
        print(letra,end=" ")
    print("")

def crear_lista_letras(palabra):
    '''    c
       _ A T _ N 
       0 1 2 3 4
      [ ['L',False], ['A',True], ['T',True], ['I',False], ['N',True]  ]
    '''
    letras = [ [letra,False] for letra in palabra]
    print(letras)
    return letras

def mostrar_palabra(lista_letras):
    for letra in lista_letras:
        if letra[1] == True:
            print(letra[0], end=" ") 
        else:
            print("_", end=" ")
    print("")

palabra_oculta = "LATIN"
numero_strikes = 6

ahorcado(palabra_oculta,numero_strikes)


    