from flask import Flask, render_template
import os, json
from flask import jsonify
from models import scripture_api

STATIC_DIR = "static"

app = Flask(__name__, template_folder='views', static_folder=STATIC_DIR)

scripture = scripture_api.scripture_api()
bible_id = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',  methods=['POST'])
def message():
    global scripture
    response = scripture.search(bible_id, "Jesus wept", limit=3, fuzziness="0")
    print(f"Response:\n{json.dumps(response, indent=4, sort_keys=True)}")
    d = "Result from api"
    return response


if __name__ == '__main__':
    app.run(debug=True)
