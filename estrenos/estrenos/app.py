from flask import Flask, render_template
from funciones import lee_archivo_csv,crea_diccionario_peliculas

app = Flask(__name__)
listado = lee_archivo_csv("lista_estrenos.csv")
diccionario_pelis = crea_diccionario_peliculas(listado)
'''
diccionario = { 'Batman':'Batman',
                'Uncharted':'Uncharted',
                'DoctorStrange':'Doctor Strange: Multiverse Madness'
              }
lista = [{'id':'Batman','titulo':'Batman'},
         {'id':'Uncharted','titulo':'Uncharted'},
         {'id':'DoctorStrange','titulo':'Doctor Strange: Multiverse Madness'}
]
'''
@app.route("/")
def index():
    return render_template("index.html",peliculas=diccionario_pelis)

@app.route("/pelicula/<id>")
def pelicula(id):
    pelicula = diccionario_pelis[id] 
    return render_template("pelicula.html",movie=pelicula)

if __name__ == "__main__":
    app.run(debug=True)