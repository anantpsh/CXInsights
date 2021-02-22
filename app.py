from flask import Flask, render_template, json, request, redirect
from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.secret_key = " "

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testingdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def main():
    return redirect('/useradmin')

@app.route('/useradmin')
def useradmin():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM ID")
    employee = cur.fetchall()
    return render_template('useradmin.html', employee=employee)

@app.route('/updateemployee', methods=['POST'])
def updateemployee():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if name == 'name':
           cur.execute("UPDATE employee SET name = %s WHERE id = %s ", (value, pk))
        elif name == 'email':
           cur.execute("UPDATE employee SET email = %s WHERE id = %s ", (value, pk))
        elif name == 'phone':
           cur.execute("UPDATE employee SET phone = %s WHERE id = %s ", (value, pk))
        mysql.connection.commit()
        cur.close()
        return json.dumps({'status':'OK'})

if __name__ == '__main__':
    app.run(debug=True)
