


class cuadrado:
    def __init__(self,lado) -> None:
     self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado
    
    def perimetro (self) -> float:
        return self.lado * 4
    
    def __str__(self)->str:
        return "el area del cuadrado es" + str(self.area()) + " y su perimetro es " + str(self.perimetro())

A=cuadrado(8)
print(A)
B=cuadrado(15.5)
print(B.area())
print(B.perimetro())