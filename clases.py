class Libro:
    def __init__(self, id, url,titulo, autor, id_categoria):
        self.id = id
        self.url = url
        self.titulo = titulo
        self.autor = autor
        self.id_categoria = id_categoria
    def __str__(self):
        return f"{self.titulo} | {self.autor}"

class Categoria:
    def __init__(self, id, categoria):
        self.id = id
        self.categoria = categoria
    def __str__(self):
        return f"{self.categoria}"

class Autor:
    def __init__(self, id, nombre):
        self.id = id
        nombre,apellido = nombre.split(" ")
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"