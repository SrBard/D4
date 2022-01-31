
from sklearn.utils import check_array
import random

def gato()->int:
    #   1 2 3     A B C
    #   4 5 6     D E F
    #   7 8 9     G H I
    #
    #   X | X | O
    #  -----------
    #   O | X | X
    #  -----------
    #   X | O | O

    tablero = "123456789"
    tablero_dicc = { llave:llave for llave in tablero}
    #tablero_dicc = { '1':'X','2':'X','3':'O','4':'O','5':'X','6':'X','7':'X','8':'O','9':'O'}

    en_juego = True
    gano = False
    empate = False
    while en_juego:
        mostrar_tablero(tablero_dicc)
        if jugadas_disponibles(tablero_dicc) == False:
            en_juego = False
            empate   = True
        else:
            casilla_elegida = False
            while casilla_elegida == False:
                opcion = input("Seleccione casilla:")
                casilla_elegida = asigna_casilla("X",opcion,tablero_dicc)

            gano = checar_si_gano("X",tablero_dicc)
            if gano == True:
                en_juego = False
            else:
                if jugadas_disponibles(tablero_dicc) == False:
                    en_juego = False
                    empate   = True
                else:
                    opcion = computadora_escoge_casilla(tablero_dicc)
                    casilla_elegida = asigna_casilla("O",opcion,tablero_dicc)
                    if checar_si_gano("O",tablero_dicc) == True:
                        en_juego = False
            
    if gano == True:
        print("¡Felicidades!")
        return 1
    else:
        if empate == True:
            print("-Empate-")
            return 0
        else:
            print("¡Lo siento!")
            return -1


def jugadas_disponibles(tablero:dict)->bool:
    #print(tablero)
    for llave,valor in tablero.items():
        if llave ==valor :
            return True
    return False

def asigna_casilla(simbolo:str,opcion:str,tablero:dict)->bool:
    '''Asigna la casilla'''
    casilla_elegida = False
    if opcion in tablero:
        if opcion == tablero[opcion]: # casilla no ocupada
            tablero[opcion] = simbolo # ocupamos la casilla
            casilla_elegida = True
        else:
            print("Casilla ocupada, elija otra")
    else:
        print("Símbolo %s no se encuentra en el tablero" % opcion)
    return casilla_elegida

def computadora_escoge_casilla(tablero_dicc):
    lista_casilla_disponibles = [k for k,v in tablero_dicc.items() if v==k]
    casilla = random.choice(lista_casilla_disponibles)
    return casilla

def mostrar_tablero(diccionario)->None:
    ''' muestra el tablero'''
    print(diccionario['1'],"|",diccionario['2'],"|",diccionario['3'])
    print("---------")
    print(diccionario['4'],"|",diccionario['5'],"|",diccionario['6'])
    print("---------")
    print(diccionario['7'],"|",diccionario['8'],"|",diccionario['9'])
    print("")

def checar_si_gano(simbolo, diccionario_tablero):
    '''checar si gano el simbolo'''
    combinaciones = [
                    [ '1','2','3'],
                    [ '4','5','6'],
                    [ '7','8','9'],
                    [ '1','4','7'],
                    [ '2','5','8'],
                    [ '3','6','9'],
                    [ '1','5','9'],
                    [ '7','5','3']       
    ]

    for combo in combinaciones:
        contador = 0
        for casilla in combo:
            if simbolo == diccionario_tablero[casilla]:
                contador += 1
        if contador == 3:
            return True
    return False

def main():
    gato()


if __name__ == "__main__":
    main()