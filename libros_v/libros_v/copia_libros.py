from clases import Libro, Categoria, Autor
import argparse
import csv

POR_AUTOR = 0
POR_TITULO = 1

def lee_archivo_csv(nombre_archivo:str)->list:
    lista_libros = []
    try:
        with open(nombre_archivo,'r',encoding='latin-1') as fh:
            csv_reader = csv.reader(fh)
            for renglon in csv_reader:
                id = renglon[0]
                url = renglon[2]
                titulo = renglon[3]
                autor = renglon[4]
                id_categoria = renglon[5]
                libro = Libro(id, url, titulo, autor, id_categoria)
                lista_libros.append(libro)
    except IOError:
        print(IOError.errno)
        print("Error no se pudo abrir el archivo:",nombre_archivo)
    return lista_libros

def leer_archivo_csv(nombre_archivo:str)->list:
    lista_libros = []
    try:
        with open(nombre_archivo,'r') as fh:
            lista = fh.readlines()
        for elemento in lista:
            lista_elementos = elemento.split(",") # separamos x coma
            id = lista_elementos[0].strip('\"')
            url = lista_elementos[2].strip('\"')
            titulo = lista_elementos[3].strip('\"')
            autor = lista_elementos[4].strip('\"')
            id_categoria = lista_elementos[5].strip('\"')
            libro = Libro(id, url, titulo, autor, id_categoria)
            lista_libros.append(libro)
    except IOError:
        print(IOError.errno)
        print("Error no se pudo abrir el archivo:",nombre_archivo)
    return lista_libros

def crea_diccionario_autores(lista:list)->dict:
    diccionario = {}
    for libro in lista:
        nombres = libro.autor.split(" ")
        nombres.append(libro.autor)
        for nombre in nombres:
            actualiza_diccionario(diccionario, nombre.upper(), libro)
    return diccionario


def crea_diccionario(lista:list,atributo:str)->dict:
    diccionario = {}
    for libro in lista:
        if (atributo == POR_TITULO):
            titulos = libro.titulo.split(" ")
            titulos.append(libro.titulo)
            llaves = titulos
        else:
            if atributo == POR_AUTOR:
                nombres = libro.autor.split(" ")
                nombres.append(libro.autor)
                llaves = nombres
        for llave in llaves:
            actualiza_diccionario(diccionario, llave.upper(), libro)
    return diccionario

def actualiza_diccionario(diccionario:dict, llave:str, libro:Libro)->None:
    if llave not in diccionario:
        diccionario[llave] = [libro]
    else:
        lista = diccionario[llave]
        lista.append(libro)

def despliega_libros(lista_libros:list)->None:
    for libro in lista_libros:
        print(libro)

def busca_x_llave(diccionario:dict, llave:str)->list:
    '''
        Busca en el diccionario la llave y retorna una lista llena
        si la llave existe, en caso contrario, retorna una lista
        vacía
    '''
    if llave in diccionario:
        lista = diccionario[llave]
    else:
        lista = []
    return lista

def main(archivo:str,autor:str,palabra:str)->None:
    lista_libros = lee_archivo_csv(archivo)
    #print(lista_libros)

    if len(autor) != 0: # buscamos por autor
        print("Libros de autor:",autor)
        d_autores = crea_diccionario(lista_libros,POR_AUTOR)
        print(len(d_autores))
        lista_resultados = busca_x_llave(d_autores,autor)
        
        despliega_libros(lista_resultados)
    else:
        d_titulos = crea_diccionario(lista_libros,POR_TITULO)
        lista_resultados = busca_x_llave(d_titulos,palabra)
        print(f"Libros con la palabra:{palabra}")
        despliega_libros(lista_resultados)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file",type=str,metavar="file",
                        default="booklisting.csv",
                        help="Archivo a leer (CSV)")
    parser.add_argument("-a","--author",type=str,metavar="author",
                        default='Emily',
                        help="Autor por buscar/encontrar")
    parser.add_argument('-t',"--title", type=str,metavar="title",
                        help="Palabra a buscar en el título")
    args = parser.parse_args()
    archivo = args.file
    autor   = args.author
    titulo  = args.title
    if autor is not None and titulo is None:
        autor = autor.upper()
        titulo = ""
        print(autor)
    if titulo is not None and autor is None:
        autor = ""
        titulo = titulo.upper()
        print(titulo)

    main(archivo,autor,titulo)  