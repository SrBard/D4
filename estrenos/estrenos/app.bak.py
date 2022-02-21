from flask import Flask, render_template

app = Flask(__name__)
diccionario = { 'id1':'Batman',
              'pelicula1':'Batman',
              'id2':'Uncharted',
              'pelicula2':'Uncharted',
              'id3':'DoctorStrange',
              'pelicula3':'Doctor Strange: Multiverse Madness'
              }
@app.route("/")
def index():
    return render_template("index.html",peliculas=diccionario)

@app.route("/pelicula/<id>")
def pelicula(id):

    return render_template("pelicula.html",identificador=id)

if __name__ == "__main__":
    app.run(debug=True)