from flask import Flask, render_template, request, redirect, url_for
from Dynamo import dynamo
from datetime import datetime

app = Flask(__name__)
dynamo = dynamo()
userName = ''

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        global userName
        userName = request.form['name']
        return redirect(url_for('index'))

@app.route('/chat', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        messages = [dict(message = msg[0], name = msg[1], timestamp = msg[2]) for msg in dynamo.getMessages()]
        sortedMessages = sorted(messages, key=lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S.%f'))
        return render_template('index.html', messages = sortedMessages)
    if request.method == 'POST':
        name = userName
        dynamo.insertNewMessage(request.form['message'], name)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
