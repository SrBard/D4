from crypt import methods
from flask import Flask, redirect, render_template,request, session
from funciones import crea_diccionario, graba_diccionario, lee_diccionario_csv, lee_diccionario_peliculas, crea_diccionario_peliculas, crea_diccionario_generos, crea_diccionario_x_anio
from passlib.hash import sha256_crypt

archivo_usuarios = 'cartelera_usuarios.csv'
app = Flask(__name__)
app.secret_key = "klNmsS679SDqWpñl"
#listado = lee_archivo_csv("cartelera_estrenos.csv")
#diccionario_pelis = crea_diccionario_peliculas(listado)
diccionario_pelis = lee_diccionario_peliculas("cartelera_estrenos.csv")
diccionario_generos = crea_diccionario_generos(diccionario_pelis)
diccionario_anios = crea_diccionario_x_anio(diccionario_pelis)
# diccionario_usuarios = {'bob': { 'nombre':'Bob Esponja',
#                                  'edad'  : '20',
#                                  'genero': 'Comedia'
#                                 }
#                         }
diccionario_usuarios = lee_diccionario_csv(archivo_usuarios)
print(diccionario_usuarios)
dicc_usuario_peli = crea_diccionario(diccionario_pelis,'usuario')

@app.route("/")
def index():
    return render_template("index.html",peliculas=diccionario_pelis)

@app.route("/pelicula/<id>")
def pelicula(id):
    if id in diccionario_pelis:
        pelicula = diccionario_pelis[id] 
        return render_template("pelicula.html",movie=pelicula)
    else:
        return render_template("no_existe.html")

@app.route("/genero/")
@app.route("/genero/<genero>")
def por_genero(genero='lista'):
    #print(f'Genero:{genero}, {type(genero)}')
    
    if genero == 'lista':
        return render_template("lista_generos.html",generos=diccionario_generos)
    else:
        print(genero)
        if genero in diccionario_generos:
            lista_peliculas = diccionario_generos[genero]
            print(lista_peliculas,type(lista_peliculas))
            return render_template("genero.html",genero=genero,peliculas=lista_peliculas)

@app.route("/anio/")
def por_anio():
    return render_template("lista_anios.html",dicc_anios=diccionario_anios)

#modificacion de usuarios
@app.route("/usuarios/")
@app.route("/usuarios/<nombre>", methods=['GET','POST'])
def usuarios(nombre='lista'):
    if request.method== 'GET':
        if nombre == 'lista':
            return render_template('lista_usuarios.html',dicc_usuarios=diccionario_usuarios)
        else:
            if nombre == 'agregar':
                return render_template('agregar_usuario.html')
    else:
        if request.method == 'POST':
            valor = request.form['enviar']
            if valor == 'Enviar':
                usuario =  request.form['username']
                nombre  =  request.form['ncompleto']
                edad    =  request.form['edad']
                genero  =   request.form['genero']
                if usuario not in diccionario_usuarios:
                    diccionario_usuarios[usuario] = {
                        'nombre': nombre,
                        'edad'  : edad,
                        'genero': genero
                    }
                graba_diccionario(diccionario_usuarios,'usuario',archivo_usuarios)
            return render_template('lista_usuarios.html',dicc_usuarios=diccionario_usuarios)

#listar peliculas por usuario
@app.route("/usuario/")
@app.route("/usuario/<usuario>")
def por_usuario(usuario='lista'):
    
    if usuario == 'lista':
        return render_template("lista_usuario.html",usuarios=diccionario_usuarios)
    else:
        if usuario in dicc_usuario_peli:
            if usuario in diccionario_usuarios:
                nombre = diccionario_usuarios[usuario]['nombre']
            else:
                nombre = ""
            lista_peliculas = dicc_usuario_peli[usuario]
            return render_template("pelicula_usuario.html",nombre_usuario=nombre,peliculas=lista_peliculas,usuario=usuario)
        else:
            msg = f'{usuario} no tiene películas en la base de datos'
            return render_template("lista_usuario.html",usuarios=diccionario_usuarios,mensaje=msg)

@app.route('/password/<username>', methods=['GET','POST'])
def modifica_password(username):
    if request.method == 'GET':
        return render_template('password.html',usuario=username)
    else:
        if request.method == 'POST':
            print(request.form.keys())
            usuario = request.form['usuario']
            texto_plano = request.form['password']
            texto_cript= sha256_crypt.hash(texto_plano)
            diccionario_usuarios[usuario]['password'] = texto_cript
            graba_diccionario(diccionario_usuarios,'usuario','cartelera_usuarios.csv')
            #print(diccionario_usuarios[usuario])
            return redirect ("/usuarios/")

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        msg = ''
        return render_template('login.html',mensaje=msg)
    else:
        if request.method == 'POST':
            #print(request.form.keys())
            usuario = request.form['usuario']
            if usuario in diccionario_usuarios:
                password_db = diccionario_usuarios[usuario]['password'] # password guardado
                password_forma = request.form['password'] #password presentado
                verificado = sha256_crypt.verify(password_forma,password_db)
                if (verificado == True):
                    session['usuario'] = usuario
                    return redirect("/")
                else:
                    msg = f'El password de {usuario} no corresponde'
                    return render_template('login.html',mensaje=msg)
            else:
                msg = f'usuario {usuario} no existe'
                return render_template('login.html',mensaje=msg)

if __name__ == "__main__":
    app.run(debug=True)