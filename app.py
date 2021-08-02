from flask import Flask, render_template, request, redirect, url_for
from Dynamo import dynamo

app = Flask(__name__)
dynamo = dynamo()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        messages = [dict(timestamp = msg[0], message = msg[1]) for msg in dynamo.getMessages()]
        return render_template('index.html', messages = messages)
    if request.method == 'POST':
        dynamo.insertNewMessage(request.form['message'])
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
