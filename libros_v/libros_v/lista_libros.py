import argparse

def lee_archivo(archivo:str)->str:
    with open(archivo,"r") as f:
        texto = f.read()
    return texto

def main(archivo:str)->None:
    t = lee_archivo(archivo)
    print(archivo,"tamaño:",len(t))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--archivo", metavar='archivo',  help="Archivo a leer", type=str,required=True)
    args = parser.parse_args()
    archivo = args.archivo
    main(archivo)