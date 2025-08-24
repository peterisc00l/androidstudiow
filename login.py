@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqn1dK4",
            password="nd0WKO3xeO",
            database="Rz8hqn1dK4"
        )
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s',(username, password))
        if account:
            print('login success')
            id account[0]
            msg = 'Logged in Successfully'
            print('login successfull')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
              msg = 'incorrect Credentials. kindly check'
              return render_template('login.html',msg=msg)
    else:
         return render_template('login.html')

from flask import Flask

app = Flask(__name__)
