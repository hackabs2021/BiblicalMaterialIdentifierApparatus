from flask import Flask, render_template, request
import os, json
from flask import jsonify
from models import scripture_api, scripture_analyzer

STATIC_DIR = "static"

app = Flask(__name__, template_folder='views', static_folder=STATIC_DIR)

scripture = scripture_api.scripture_api()

nlp = scripture_analyzer.ScriptureAnalyzer()
nlp.put_in_text_data()
nlp.find_10_topics()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',  methods=['POST'])
def message():
    global scripture
    sentence = request.form['message']
    print(sentence)
    phrase = nlp.prepare_text_for_lda(sentence)
    print(phrase)
    bible_id = '65eec8e0b60e656b-01'
    count = scripture.count(bible_id, phrase)
    
    response = scripture.search(bible_id, phrase, limit=5, fuzziness="0")
    print(f"Response:\n{json.dumps(response, indent=4, sort_keys=True)}")
    d = "Result from api"
    return {'count': len(response), 'response': response, 'full_count': count}


if __name__ == '__main__':
    app.run(debug=True)
