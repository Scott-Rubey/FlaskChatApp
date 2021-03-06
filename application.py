from flask import Flask, render_template, request, redirect, url_for, session
from Dynamo import dynamo
from datetime import datetime

application = Flask(__name__)
application.config['SECRET_KEY'] = 'g_w8Rjd1yspgOEENMvogbg'
dynamo = dynamo()

@application.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        userName = request.form['name']
        session['USERNAME'] = userName
        return redirect(url_for('index'))

@application.route('/chat', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', messages = getSortedMessages())

    if request.method == 'POST':
        name = session.get('USERNAME')
        dynamo.insertNewMessage(request.form['message'], name)
        return redirect(url_for('index'))

#sort messages based on timestamp
def getSortedMessages():
    messages = [dict(message=msg[0], name=msg[1], timestamp=msg[2]) for msg in dynamo.getMessages()]
    sortedMessages = sorted(messages, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S.%f'))
    return sortedMessages

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug = True)
