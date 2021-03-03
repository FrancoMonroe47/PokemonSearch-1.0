from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import requests

app = Flask(__name__)

app.config ['MYSQL_HOST']='localhost'
app.config ['MYSQL_USER']='FrancoMonroy'
app.config ['MYSQL_PASSWORD']='@FrancoBB47'
app.config ['MYSQL_DB']='francomonroy'
mysql= MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registro', methods=['POST'])
def registro():
    if request.method == 'POST':
        nombre_u = request.form ['nombre']
        contraseña_u = request.form ['contraseña']
        bd=mysql.connection.cursor()
        bd.execute('INSERT INTO usuarios(Nombre, Contraseña) VALUES(%s,%s)',
        (nombre_u, contraseña_u))
        mysql.connection.commit()
        return 'Registrado con exito'
        
@app.route('/registrar', methods=['GET','POST'])
def registrar():
    return render_template('registrar.html')

@app.route('/loggin', methods=['POST'])
def loggin():
    nombre_u = request.form ['nombre']
    contraseña_u = request.form ['contraseña']
    bd=mysql.connection.cursor()
    busca_u = ("SELECT * FROM usuarios WHERE Nombre = ? AND Contraseña = ?")
    bd.execute(busca_u, [(nombre_u), (contraseña_u)])
    resul_u= bd.fetchall()
    if resul_u:
        flash('Bienvenido')
        return redirect(url_for('index'))
    else:
        flash('Usuario/contraseña Incorrectos')
        return redirect(url_for('logeo'))

@app.route('/logeo', methods =['GET','POST'])
def logeo():
    return render_template('logeo.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(port= 443, debug=True)
        
url_api="https://pokeapi.co/api/v2/pokemon/"

def pokesearch():
    Nombre_pokemon = input("Nombre del pokemon ")
    Url_Nombre_pokemon = url_api + Nombre_pokemon
    Datos_pokemon= get_pokemon_data(Url_Nombre_pokemon)
    print(Datos_pokemon)

def get_pokemon_data(url_pokemon=''):
    Pokemon_data = {
        "id":'',
        "Nombre":'',
        "Tamaño":'',
        "Habilidades":'',
        "Tipo":'',
        "Peso":""
    }
    
    respuesta= requests.get(url_pokemon)
    Datos_pokemon = respuesta.json()
    #nombres en http://jsonviewer.stack.hu/ usando https://pokeapi.co/api/v2/pokemon/charizard
    Pokemon_data ['id'] = Datos_pokemon['id']
    Pokemon_data ['Nombre'] = Datos_pokemon['name']
    Pokemon_data ['Tamaño'] = Datos_pokemon['height']
    Pokemon_data ['Peso'] = Datos_pokemon['weight']
    Pokemon_data ['Habilidades'] = len(Datos_pokemon['abilities'])
    Pokemon_data ['Tipo'] = Datos_pokemon['types']
    return Pokemon_data

    
