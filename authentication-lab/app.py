from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyCP303DRxRl0QssqpUMtOGs_gWs6ZhMeJA",
  "authDomain": "maya-bsharat.firebaseapp.com",
  "projectId": "maya-bsharat",
  "storageBucket": "maya-bsharat.appspot.com",
  "messagingSenderId": "930810515359",
  "appId": "1:930810515359:web:379f203599d60a0f3b77aa",
  "measurementId": "G-6HSZTJNWYV",
  "databaseURL":"https://console.firebase.google.com/project/maya-bsharat/database/maya-bsharat-default-rtdb/data/~2F"

}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app=Flask(__name__)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error=""
    if request.method == 'post':
        email = request.form['email']
        password = request.form['password']

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error =""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)