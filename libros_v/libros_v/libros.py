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

def main(**kwargs:dict)->None:
    archivo = kwargs['archivo']
    autor = kwargs['autor']
    titulo = kwargs['titulo']
    lista_libros = lee_archivo_csv(archivo)
    #print(lista_libros)
    lista_final = []
    encabezado = ""

    if autor is not None: # buscamos por autor
        encabezado = f"Libros de autor:{autor}"
        d_autores = crea_diccionario(lista_libros,POR_AUTOR)
        lista_autor = busca_x_llave(d_autores,autor.upper())
        lista_final = lista_autor        
    if titulo is not None: # buscamos por titulo
        d_titulos = crea_diccionario(lista_libros,POR_TITULO)
        lista_titulos = busca_x_llave(d_titulos,titulo.upper())
        encabezado = f"Libros con la palabra:{titulo}"
        lista_final = lista_titulos
    if autor is not None and titulo is not None:
        encabezado = f"Libros de autor:{autor} y con la palabra:{titulo}"
        #lista_final =lista_autor + lista_titulos # unión de listas | union de conjuntos
        lista_final = list(set(lista_autor).intersection(set(lista_titulos))) # intersección de conjuntos | autores y titulos
        
    print(encabezado)
    despliega_libros(lista_final)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file",type=str,metavar="file",
                        default="booklisting.csv",
                        help="Archivo a leer (CSV)")
    parser.add_argument("-a","--author",type=str,metavar="author",
                        help="Autor por buscar/encontrar")
    parser.add_argument('-t',"--title", type=str,metavar="title",
                        
                        help="Palabra a buscar en el título")
    args = parser.parse_args()
    archivo = args.file
    autor   = args.author
    titulo  = args.title
    kwargs = {          #kw = keyword / args = argument
        "archivo":archivo,
        "autor":autor,
        "titulo":titulo
    }
    main(**kwargs)  