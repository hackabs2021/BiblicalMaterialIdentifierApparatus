from flask import Flask, render_template
import os
from flask import jsonify

STATIC_DIR = "static"

app = Flask(__name__, template_folder='views', static_folder=STATIC_DIR)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',  methods=['POST'])
def message():
    d = "Result from api"
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug=True)
