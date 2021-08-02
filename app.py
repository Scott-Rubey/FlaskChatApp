from flask import Flask
from flask import render_template
from .dynamo import dynamo

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    messages = [dict(timestamp = msg[0], message = msg[1]) for msg in dynamo.getMessages()]
    return render_template('index.html', messages = messages)

if __name__ == '__main__':
    app.run(debug = True)
