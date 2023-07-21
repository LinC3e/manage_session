from flask import Flask , render_template, request , redirect, url_for
from config import config
import db

app = Flask(__name__)

@app.route('/')
def home():
    db.conectar()
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()