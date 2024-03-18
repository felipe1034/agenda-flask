from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskusuarios'
mysql = MySQL(app)

#settings
app.secret_key = 'magaly2024'

#--------------------------------------------------#
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM personas')
    data = cursor.fetchall()
    return render_template('index.html',usuarioos = data)

#--------------------------------------------------#
@app.route('/add_usuario', methods=['POST'])
def add_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        contrasena= request.form['contrasena']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO personas (nomper, apellidoper, emailper, direccionper, telefonoper, usuarioper, contrasenaper) VALUES (%s, %s, %s, %s, %s, %s, %s)',(nombre,apellido,email,direccion,telefono,usuario,contrasena))
        mysql.connection.commit()
        flash('usuario registrado correctamente')
        return redirect(url_for('index'))
#--------------------------------------------------#
@app.route('/edit/<id>')
def get_usuario(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM personas WHERE polper = %s',(id))
    data = cursor.fetchall()
    return render_template('edit.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_usuario(id):
    if request.method == 'POST':
        nombreper = request.form ['nombre']
        apellidoper = request.form ['apellido']
        emailper = request.form ['email']
        direccionper = request.form ['direccion']
        telefonoper = request.form ['telefono']
        usuarioper = request.form ['usuario']
        contrasenaper = request.form ['contrasena']
        cur= mysql.connection.cursor()
        cur.execute("""UPDATE personas SET 
                    nombreper = %s, 
                    apellidoper = %s, 
                    emailper =%s, 
                    direccionper =%s, 
                    telefonoper =%s, 
                    usuarioper =%s, 
                    contrasenaper =%s
                    WHERE polper = %s""", (nombreper, apellidoper, emailper, direccionper, telefonoper, usuarioper, contrasenaper, id ))
        mysql.connection.commit()
        flash('Usuario actualizado satisfactoriamnete')
        return redirect(url_for('index'))


#--------------------------------------------------#
@app.route('/delete/<string:id>')
def delete_usuario(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM personas WHERE polper ={0}'.format(id))
    mysql.connection.commit()
    flash ('Contacto removido satisfactoria mente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,port=5000)
 


   
