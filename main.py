from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route("/details", methods=['POST', 'GET'])
def details():
    user_name = request.form['user_name']
    phone_number = request.form['contact_number']
    number_of_items = request.form['number_of_items']
    total_amout = request.form['amount']
    current_date = request.form['current_date']
    mydb = mysql.connector.conect(
        host='remotemysql.com',
        user='uLj9FaRVB',
        password='qQvo5rGf3i',
        database='uLj9FaRVB'
    mycursor = mydb.cursor()
    mycursor.execute('CRATE TABLE Customer_Details (Customer_Name varchar(225),phone_Number varchar(10), Number_of_Items int(11), Total_Amount int (11), Date_of_Purchase date)'
                       )
        
    mycursor.execute(
        'INSERT INTO Customer_Details VALUES (%s, %s, %s, %s, %s)',
        (user_name, phone_number, number_of_items, total_amout,
          current_date ))
            mydb.commit()
            return render_template('page.html')

@app.route('/winner', methods=['POST', 'GET'])
def winner():
    mydb = mysql.connector.connect( host='remotemysql.com',
                                    user='uLj9FaRVB',
                                    password='qQvo5rGf3i',
                                    database='uLj9FaRVB')  
    mycursor = mydb.cursor()
    mycursor.execute(
        'SELECT * FROM Customer_Details WHERE Date_of_Purchase ='
        'CURRENT_DATE ORDER BY Total_Amount DESC'
             )
             account = mycursor.fetchone()
             print(account)
             if account:
                 user_name = accout[0]
                 phone_number = account[0]
                 return render_template('page.html'
                                        user_name=user_name
                                        phone_number=phone_number)
            else:
            return render_template('page.html')

@app .route('/')
def index():
    return render_template('index.html')



app.run(host='0.0.0.0', port=800)

)