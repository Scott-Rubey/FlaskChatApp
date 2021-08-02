from flask import Flask, render_template
from Dynamo import dynamo

app = Flask(__name__)
dynamo = dynamo()

@app.route('/', methods = ['GET', 'POST'])
def index():  # put application's code here
    messages = [dict(timestamp = msg[0], message = msg[1]) for msg in dynamo.select()]
    return render_template('index.html', messages = messages)

if __name__ == '__main__':
    app.run(debug = True)
