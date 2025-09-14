from flask import*
from flask_mail import*
from random import*

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'pete6767676@gmail.com'
app.config["MAIL_PASSWORD"] = '6666677777778910'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

otp = randint(000000,999999)

@app.route('/verify',methods = ["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP',sender = 'peterand156967@gmail.com', recipients = [email])
    msg.body = str(otp)
    Mail.send(msg)
    return render_template('page.html')

@app.route('/vaildate',method = ['POST'])
def vaildate():
    user_otp = request.form["otp"]
    if otp == int(user_otp):
        return "<h3>email verification successful</h3>"
    else:
        return "<h3>Verification failed otp does not match</h3>"

@app.route('/')
def index():
    return render_template('index.html')



app.run(host='0.0.0.0', port=8080)