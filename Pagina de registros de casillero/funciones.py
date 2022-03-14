import csv

def lee_archivo_csv(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista de registros
    '''
    lista= []

    try:
        with open(archivo,'r',encoding='UTF-8') as fh:
            csv_reader = csv.reader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    print (lista)
    return lista

def disponibles_casilleros(registros:list)->list:
    
    casi_usados= []
    casi = []
    for renglon in registros:
        if len(renglon) != 0:
            casi_usados.append(renglon[3])
    casi_usados.pop(0)
    for i in range(12001):
        if i < 199:
            casi.append("A-"+f'{i+1}')
        if  i > 199 and i < 400:
            casi.append("B-"+f'{i}')
        if  i > 399 and i < 600:
            casi.append("C-"+f'{i}')
        if  i > 599 and i < 800:
            casi.append("D-"+f'{i}')
        if  i > 799 and i < 1000:
            casi.append("E-"+f'{i}')
        if  i > 999 and i < 1201:
            casi.append("F-"+f'{i}')
   
    disponibles = sorted(set(casi_usados) ^ set(casi))
    
    return disponibles
def Registar_casi(DATA:list):
    print(DATA)
    with open('Registros.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(DATA)
        f.close()

