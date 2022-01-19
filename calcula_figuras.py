import figuras

def main():
    print("calcula el area y el perimetro de las figuras")
    corriendo = True
    
    while corriendo:

        respuestas = input ("Calcular Cuadrado o Rectangulo" )
        if respuestas == "C":
            lado = input ("cuanto mide el lado?")
            lado = float(lado)
            fig = figuras.cuadrado(lado)
            print (fig)
        else:
            if respuestas == "R":
                base = input ("cual es la base?: R")
                altura = input( "cual es la altura?: ")
                base = float (base)
                altura =float(altura)
                fig= figuras.rectangulo(base,altura)
                print (fig)
           
            else:
                if respuestas =="S":
                   corriendo = False
    
    print ("gracias por jugar")

if __name__ == "__main__":
    main()