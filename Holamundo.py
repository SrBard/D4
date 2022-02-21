from flask import Flask

app = Flask(__name__)

app.route('/')
def index():
    return 'hola mundo'

app.route('/about')
def about():
    return 'paigna de preguntas'

if __name__=='__name__':
    app.run(debug=True)    