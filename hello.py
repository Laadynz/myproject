#Para activar el ambiente usamos: > .venv\Scripts\activate
# Para arrancar el proyecto se usa: flask --app hello run --debug
#los comandos anteriores son para CMD

from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    # Conexión a la base de datos
    #mycursor = mydb.cursor()
    

    #Obtener datos de la base de datos
    #mycursor.execute('SELECT * FROM productos')
    #productos = mycursor.fetchall()
    #Cerrar la conexión
    #mycursor.close()
    #print("bien")
    #return("todo bien")
    #return render_template("menu.html",productos=productos)

    return render_template("menu.html")

@app.route('/cp')
def page1():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM productos')
    productos = mycursor.fetchall()
    mycursor.close()
    return render_template("catalagoProductos.html",productos=productos)

@app.route('/cu')
def page2():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM usuarios')
    usuarios = mycursor.fetchall()
    mycursor.close()
    return render_template("catalogoUsuarios.html",usuarios=usuarios)

@app.route('/cc')
def page3():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM clientes')
    clientes = mycursor.fetchall()
    mycursor.close()
    return render_template("catalogoClientes.html",clientes=clientes)

if __name__ == '__main__':
    app.run()