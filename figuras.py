


class cuadrado:
    def __init__(self,lado) -> None:
     self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado
    
    def perimetro (self) -> float:
        return self.lado * 4
    
    def __str__(self)->str:
        return "el area del cuadrado es" + str(self.area()) + " y su perimetro es " + str(self.perimetro())
class rectangulo:
    def __init__(self,base,altura) -> None:
        self.base = base
        self.altura = altura

    
    def area(self) -> float:
        return self.base * self.altura
    
    
    def perimetro(self) -> float:
        return (self.base * 2) + (self.altura *2)
    
    
    def __str__(self) -> str:
        return "El area del rectangulo es: " + str(self.area()) + " y su perimetro es: " + str(self.perimetro())


def main():
    A=cuadrado(8)
    print(A)
    B=cuadrado(15.5)
    print(B.area())
    print(B.perimetro())
    C = rectangulo(5,5)
    print(C)
    if __name__ == "__main__":
        main()