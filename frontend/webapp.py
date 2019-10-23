import request
import urllib
from flask import Flask, render_template

app = Flask(__name__)

# routing home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='home')

# routing about page
@app.route('/about')
def about():
    return render_template('about.html', title='about')

# routing contact page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

# routing login
@app.route('/login')
#@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html',title='login')

if __name__ == '__main__':
    app.run(debug=True)
