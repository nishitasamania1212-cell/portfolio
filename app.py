from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# EMAIL CONFIG
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'nishitasamania1212@gmail.com'
app.config['MAIL_PASSWORD'] = 'rryssblvicwtynlx'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        subject=f"New message from {name}",
        sender='nishitasamania1212@gmail.com',
        recipients=['nishitasamania1212@gmail.com'],
        body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
    )

    mail.send(msg)

    return "Message Sent Successfully 💖"

if __name__ == '__main__':
    app.run(debug=True)