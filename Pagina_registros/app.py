
from cgitb import html
from distutils.log import debug
from flask import Flask, render_template,request,flash,redirect,url_for
from sympy import true
from funciones import *
from waitress import serve
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Asus Laptop/Documents/Proyectos_vscode/d4/D4/Pagina_registros/certificados'

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/", methods=['GET','POST'])
def index():
        if request.method== 'GET':
            lista=lee_archivo_csv("Registros.csv")
            casi= disponibles_casilleros(lista)
            return render_template("index.html",disponibles=casi)
        if request.method == 'POST':
     
                DATA= []
                DATA.append(request.form['nombres'])
                DATA.append(request.form['apellidos'])
                DATA.append(request.form['num_em'])
                DATA.append(request.form['Casilleros'])
                print(DATA)
                if DATA[0] != "" and DATA[1] != "" and DATA[2] != "" and DATA[3] !="" and si_esta_disponible(DATA[3]) :    
                    print(len(DATA[2]))
                    if len(DATA[2]) == 6 and DATA[2].isdigit():
                        Registar(DATA,'Registros.csv')
                        flash("El registros se hizo con exito", "success")
                        lista=lee_archivo_csv("Registros.csv")
                        casi= disponibles_casilleros(lista)
                        return render_template("index.html",disponibles=casi)
                    else: 
                        flash("Su numero de Empleado es erroneo", "warning")
                        lista=lee_archivo_csv("Registros.csv")
                        casi= disponibles_casilleros(lista)
                        return render_template("index.html",disponibles=casi)
                else:
                    flash("Tienes que llenar todos los campos o el caillero ya esta ocupado", "warning")
                    lista=lee_archivo_csv("Registros.csv")
                    casi= disponibles_casilleros(lista)
                    return render_template("index.html",disponibles=casi)
        
        lista=lee_archivo_csv("Registros.csv")
        casi= disponibles_casilleros(lista)
        return redirect("index.html",disponibles=casi)

@app.route("/vacunados", methods=['GET','POST'])
def vacunados():
    if request.method== 'GET':
        return  render_template("vacunados.html")
    if request.method== 'POST':
        valor = request.form['Upload']
        if valor == "Guardar":
                DATA= []
                DATA.append(request.form['nombres'])
                DATA.append(request.form['apellidos'])
                DATA.append(request.form['num_em'])
                
                
                if DATA[0] != "" and DATA[1] != "" and DATA[2] != "":    
                    
                    if len(DATA[2]) == 6 and DATA[2].isdigit():
                        if  'btnradio' in request.form:
                            if  request.form['btnradio'] =="Si":
                            
                                DATA.append('Si')
                                if 'customFile' in request.files:
                
                                    f = request.files['customFile']
                                    if f != None:
                    
                                        if f and allowed_file(f.filename):
                                            Registar(DATA,'Registros_vacunados.csv')
                                            num_em = request.form['num_em']
                                            formato=formato_file(f.filename)
                                            filename = secure_filename(f.filename)
                                            name_new =num_em+"."+formato
                                            file_dress= os.path.join(app.config['UPLOAD_FOLDER'], filename)
                                            f.save(file_dress)
                       
                                            os.rename(file_dress, os.path.join(app.config['UPLOAD_FOLDER'],name_new))
                                            flash("El registro fue exitoso", "success")
                                            return redirect(request.url)
                                        else:
                                            flash("Solo se aceptan archivos 'pdf, png, jpg, jpeg", "warning")
                                            return  redirect(request.url) 
                                    else:
                                        flash("No hay ningun archivo seleccionado", "warning")
                                        return  redirect(request.url)
                                else:
                                     return redirect(request.url)   
                            else:
                               
                                    DATA.append("No")
                                    Registar(DATA,'Registros_vacunados.csv')
                                    flash("Se registro con exito", "success")
                                    return  redirect(request.url)
                                
                        else:
                            flash("Tiene que contestar a la pregunta", "warning")
                            return  redirect(request.url)       
                    else:
                        flash("Su numero de empleado es erroneo", "warning")
                        return  redirect(request.url) 
                else:
                    flash("Tiene que llenar todos los campos", "warning")
                    return  redirect(request.url)

if __name__ == "__main__":
    
    serve(app, host="192.168.100.171", port=5000)