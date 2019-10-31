import requests
import secrets
import urllib
from flask import Flask, render_template, request, redirect, url_for, session
#from flask_googlecharts import BarChart

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
#charts = GoogleCharts(app)
#charts.init_app(app)

'''
    This the home page method.
    It only renders the layout.
    Not needed, but might be useful if other basic things are needed to be sent to the client.
'''
# routing home page
@app.route('/')
def home():
    return render_template('layout.html')

'''
    This function verifies that the user has entered the neccessary info before going any further
    required info: server address & pin.
    for now it just checks for the parameters existence.
'''
def verify_session():
    addr = session.get('addr')
    pin = session.get('pin')
    if addr==None or pin==None:
        session['message']='please use a valid server address and a pin'
        return False
    return True

'''
    This method takes the client's server address and a pin.
    It then routes the client to the participation page (settings).
'''
# routing register page
@app.route('/register', methods=['GET','POST'])
def register():
    if(request.method=='POST'):
        addr=request.form['addr_server']
        pin=request.form['pin']
        session['addr']=addr
        session['pin']=pin
        return redirect(url_for('settings'))
    

    message=session.pop('message',None)
    return render_template('register.html',message=message)


'''
    This method takes takes the amount of participation desired by the user.
    It first checks for a valid server address and a valid pin.
'''
# routing settings page
@app.route('/settings', methods=['GET','POST'])
def settings():
    if request.method=='POST':
        # check for mission info
        # to avoid user routing before filling addr & pin
        if not verify_session():
            return redirect(url_for('register'))
        return redirect(url_for('status'))
    return render_template('settings.html')

'''
    This function is resposible for graphing the grid to the client. 
    It returns a visual representation of the grid and the user's participation.
    It will probable use google chart api to create the chart.
'''
# routing status page
@app.route('/status')
def status():
    if not verify_session():
        return redirect(url_for('register'))
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug=True)
