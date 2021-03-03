from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import requests


app = Flask(__name__)

app.config ['MYSQL_HOST']='localhost'
app.config ['MYSQL_USER']='FrancoMonroy'
app.config ['MYSQL_PASSWORD']='@FrancoBB47'
app.config ['MYSQL_DB']='francomonroy'
mysql= MySQL(app)

app.secret_key = 'mysecretkey'
url_api="https://pokeapi.co/api/v2/pokemon/"

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
        flash("Registrado con exito")
        return redirect(url_for('index'))
        
@app.route('/registrar', methods=['GET','POST'])
def registrar():
    return render_template('registrar.html')

@app.route('/loggin', methods=['POST'])
def loggin():
   if request.method == 'POST':
        nombre_u = request.form ['nombre']
        contraseña_u = request.form ['contraseña']
        bd=mysql.connection.cursor()
        bd.execute("SELECT Nombre FROM usuarios")
        nombre_bd = bd.fetchone()
        bd.execute("SELECT Contraseña FROM usuarios")
        contraseña_bd = bd.fetchone()
        print(contraseña_bd,nombre_bd)
        if nombre_u == nombre_bd and contraseña_u == contraseña_bd:
            mysql.connection.commit()
            return 'bienvenido'
        else:
            flash('usuario/Contraseña incorrectos')
            return redirect(url_for('login'))

@app.route('/login', methods =['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/pokesea', methods=['GET','POST'])
def pokesea():
    if request.method == 'POST':
        Nombre_pokemon = request.form ['pokemon']
        Url_Nombre_pokemon = url_api + Nombre_pokemon
        Datos_pokemon= get_pokemon_data(Url_Nombre_pokemon)
        pokemon_type = [types ['type']['name'] for types in Datos_pokemon ['Tipo']]
        print(Datos_pokemon)
        print(pokemon_type)
    return render_template('perfil.html', pokemon= Datos_pokemon) 

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

if __name__ == '__main__':
    app.run(port= 443, debug=True)  
