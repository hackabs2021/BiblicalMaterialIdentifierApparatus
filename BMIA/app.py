from flask import Flask, render_template, request
import os, json
from flask import jsonify
from models import scripture_api, scripture_analyzer

STATIC_DIR = "static"

app = Flask(__name__, template_folder='views', static_folder=STATIC_DIR)

# Scripture API setup
scripture = scripture_api.scripture_api()
api_key = scripture_api.retrieve_api_key()
scripture.authenticate(api_key)
scripture.set_bible('de4e12af7f28f599-01') # King James (Authorised) Version

nlp = scripture_analyzer.ScriptureAnalyzer()
nlp.put_in_text_data()
nlp.find_10_topics()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',  methods=['POST'])
def message():
    global scripture

    # Execute NLP
    sentence = request.form['message']
    print(sentence) # TEMP - Debug
    phrase = nlp.prepare_text_for_lda(sentence)
    print(phrase) # TEMP - Debug

    response = scripture.search(phrase, limit=5, fuzziness="0") # Search phrase

    # Count verses
    count = 0
    if "data" in scripture:
        count = len(scripture["data"])

    print(f"Response:\n{json.dumps(response, indent=4, sort_keys=True)}") # TEMP - Debug

    # Result from API
    return {'count': len(response), 'response': response, 'full_count': count}


if __name__ == '__main__':
    app.run(debug=True)
