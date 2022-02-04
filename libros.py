from clases import Libro, Categoria, Autor

def lee_archivo_csv(nombre_archivo:str)->list:
    lista_libros = []
    try:
        with open(nombre_archivo,'r') as fh:
            lista = fh.readlines()
        for elemento in lista:
            lista_elementos = elemento.split(",")
            id = lista_elementos[0]
            url = lista_elementos[2]
            titulo = lista_elementos[3]
            autor = lista_elementos[4]
            id_categoria = lista_elementos[5]
            libro = Libro(id,url,titulo,autor,id_categoria)
            lista_libros.append(libro)

    except:
        print("Error no se pudo abrir el archivo: ",nombre_archivo)
    return lista_libros

def crea_diccionario_autores(lista:list)->None:
    diccionario = {}
    for libro in lista:
        if libro.autor not in diccionario:
            diccionario[libro.autor] = [libro]
        else:
            lista = diccionario[libro.autor]
            lista.append(libro)
        return diccionario

def main(archivo:str)->None:
    lista_libros = lee_archivo_csv(archivo)
    print(lista_libros)
    d_autores = crea_diccionario_autores(lista_libros)
    print(d_autores)

if __name__ == "__main__":
    main("shortbooklist.csv")