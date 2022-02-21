import csv

class Pelicula():
    def __init__(self,id,titulo,link_foto,fecha_estreno,descripcion):
        self.id = id
        self.titulo = titulo
        self.link_foto = link_foto
        self.fecha_estreno = fecha_estreno
        self.descripcion   = descripcion
    def __str__(self):
        return f'{self.titulo} - {self.fecha_estreno}'

def lee_archivo_csv(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista de registros
    '''
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.reader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista

def crea_diccionario_peliculas(lista:list) -> dict:
    ''' Cicla la lista de peliculas para crear objetos Pelicula y agregarlos
        al diccionario de peliculas. Regresa un diccionario de películas
    '''
    diccionario_peliculas = {}
    for pelicula in lista:
        id = pelicula[0]
        titulo = pelicula[1]
        link = pelicula[2]
        fecha = pelicula[3]
        trama = pelicula[4]
        movie = Pelicula(id,titulo,link,fecha,trama)
        if id not in diccionario_peliculas:
            diccionario_peliculas[id] = movie
    return diccionario_peliculas


if __name__ == "__main__":
    listado = lee_archivo_csv("lista_estrenos.csv")
    for pelicula in listado:
        print(pelicula[1])
    diccionario = crea_diccionario_peliculas(listado)
    print(diccionario['SalemsLot'].descripcion)
        