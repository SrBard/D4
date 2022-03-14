
from flask import Flask, render_template,request,flash,redirect
from funciones import lee_archivo_csv,disponibles_casilleros,Registar_casi


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
lista=lee_archivo_csv("Registros.csv")
casilleros= disponibles_casilleros(lista)



@app.route("/", methods=['GET','POST'])
def index():
        if request.method== 'GET':
            lista=lee_archivo_csv("Registros.csv")
            casi= disponibles_casilleros(lista)
            return render_template("index.html",disponibles=casi)
        if request.method == 'POST':
            
            valor = request.form['Regis']
            if valor == 'Registrar':
                
                DATA= []
                DATA.append(request.form['nombres'])
                DATA.append(request.form['apellidos'])
                DATA.append(request.form['num_em'])
                DATA.append(request.form['Casilleros'])
                print(DATA)
                if DATA[0] != "" and DATA[1] != "" and DATA[2] != "" and DATA[3] !="":    
                    Registar_casi(DATA)
                    lista=lee_archivo_csv("Registros.csv")
                    casill= disponibles_casilleros(lista)
                    flash("El registros se hizo con exito", "success")
                    lista=lee_archivo_csv("Registros.csv")
                    casi= disponibles_casilleros(lista)
                    return render_template("index.html",disponibles=casi)
                else:
                    flash("Tienes que llenar todos los campos", "warning")
                    lista=lee_archivo_csv("Registros.csv")
                    casi= disponibles_casilleros(lista)
                    return render_template("index.html",disponibles=casi)
        
    

if __name__ == "__main__":
    app.run(debug=True)