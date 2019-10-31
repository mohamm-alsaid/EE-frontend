import requests
import secrets
import urllib
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# routing home page
@app.route('/')
def home():
    return render_template('layout.html')

# routing register page
@app.route('/register', methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        addr=request.form['addr_server']
        pin=request.form['pin']
        session['addr']=addr
        session['pin']=pin
        return redirect(url_for('settings'))
    
    return render_template('register.html')


# routing settings page
@app.route('/settings', methods=['GET','POST'])
def settings():
    if request.method=='POST':
        val = request.form['participation']
        print(val)
        print(session['pin'])
        print(session['addr'])
        return redirect(url_for('status'))
    return render_template('settings.html')

# routing status page
@app.route('/status')
def status():
    # will graph the status of the grid?
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug=True)
