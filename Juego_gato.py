from gato import gato


def main():
    estado_juego = { 0: 0,
    1: 0,
    -1: 0}
    en_juego = True
    while en_juego == True:
        resultado = gato()
        estado_juego[resultado] += 1
        despliega_resultados(estado_juego)
        seguir_jugando = input("¿Quieres seguir jugando (S/N):")
        seguir_jugando = seguir_jugando.upper()
        if seguir_jugando == "N":
            en_juego = False
        
def despliega_resultados(estado_juego):
    diccionario_resultados = { 1:'ganados:', 0:'empates:',-1:'perdidos:'}
    for llave,valor in estado_juego.items():
        print(diccionario_resultados[llave],valor,end=" ")
    print("")




if __name__ == "__main__":
    main()