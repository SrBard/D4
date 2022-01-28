from operator import truediv
from pickle import TRUE
import funciones

def ahorcado(palabra:str,num_strikes:int)->None:
    palabra = palabra.upper()
    lista   = [ [x,False] for x in palabra]
    num_letras = len(palabra)
    ya_gano    = False
    abcdario  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = { c:False for c in palabra}
    intentos = 0
    letras_usadas = []
    #diccionario = { 'V':[[0],False], "I":[[1],False], "E":[[2,5],False], "R":[[3],False], "N":[[4],False], "S":[[6],False]}
    while intentos<=num_strikes and ya_gano==False:
        mostrar_pisos(lista)
        mostrar_strikes(intentos,num_strikes)
        mostrar_abc(abcdario,letras_usadas)
        respuesta = input("Ingrese palabra o letra:")
        respuesta = respuesta.upper()
        if (len(respuesta)>1):
            if (respuesta == palabra):
                ya_gano = True
                print("¡Felicidades!, adivinaste la palabra")
            else:
                intentos += 1
                print("Palabra incorrecta")
        else:
            letra = respuesta[0]
            if letra not in letras_usadas:
                letras_usadas.append(letra)
                bandera = False
                for letra_lista in lista:
                    if letra == letra_lista[0]:
                        if letra_lista[1]== False:
                            letra_lista[1]= True
                            bandera = True
                            ya_gano = revisar_lista(lista)
                if bandera == False:
                    intentos += 1
            else:
                print("Ya usaste la letra:",letra)
    if ya_gano == True:
            print("¡Felicidades!")
    else:
        print("Perdiste")
        print("La palabra oculta era:",palabra)
    return ya_gano
           
def revisar_lista(lista:list)->bool:
    longitud_true = 0
    for elemento in lista:
        if elemento[1] == True:
            longitud_true +=1
    if longitud_true == len(lista):
        return True
    else:
        return False


def mostrar_strikes(intentos:int, num_strikes:int)->None:
    vidas = "O"
    vidas_strike ="X"
    for i in range(num_strikes):
        if intentos > 0:
            intentos = intentos -1
            print(vidas_strike,end=" ")
        else:
            print(vidas,end=" ")
    print("")

def mostrar_abc(cadena_abc:str,letras_usadas:list)->None:
    for letra in cadena_abc:
        if letra in letras_usadas:
            print("*",end=" ")
        else:
            print(letra, end=" ")
    print("")

def mostrar_pisos(lista:list)->None:
    for elemento in lista:
        if elemento[1] == True:
            print(elemento[0],end=" ")
        else:
            print("_", end=" ")
    print("")

# palabra = "VIERNES"
# lista   = [ [x,False] for x in palabra]
# print(lista)
# lista[1] = ['I',True]
# #['V', 'I', 'E', 'R', 'N', 'E', 'S']
# #[['V',False], ['I',False], ['E',False], ]
# mostrar_pisos(lista)
# letras_usadas = ["L","V"]
# letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# mostrar_abc(letras,letras_usadas)
# intentos = 0
# num_strikes = 6
# mostrar_strikes(intentos,num_strikes)
def main()->None:
    ahorcado("LATIN",6)

if __name__ == "__main__":
    main()

    