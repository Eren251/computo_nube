from flask import Flask
#crear isinstancia
app = Flask(__name__)
#ruta raiz

@app.route('/')
def hola_mundo():
    return 'Hola mundo'

@app.route('/alumnos')
def getAlumnos():
    return 'Aqui van los alumnos'

if __name__ == '__main__':
    app.run(debug=True)
