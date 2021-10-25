from flask import Flask, render_template, request
import os, json
from flask import jsonify
from models import scripture_analyzer
from models.scripture_api import scripture_api , replace_suffix_with_wildcard, retrieve_api_key


# Clear console
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # For Windows, use cls
        command = 'cls'
    os.system(command)


## Setup
clear_console()
print("Getting things ready!")

# Flask setup
STATIC_DIR = "static"
app = Flask(__name__, template_folder='views', static_folder=STATIC_DIR)

# Scripture API setup
scripture = scripture_api()
api_key = retrieve_api_key()
scripture.authenticate(api_key)
scripture.set_bible('de4e12af7f28f599-01') # King James (Authorised) Version

# NLP setup
nlp = scripture_analyzer.ScriptureAnalyzer()
nlp.put_in_text_data()
nlp.find_10_topics()

clear_console()
## Setup complete


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message',  methods=['POST'])
def message():
    global scripture

    sentence = request.form['message'] # Get input from form
    print(f"Sentence: {sentence}") # TEMP - Debug

    # Execute NLP
    keywords = nlp.prepare_text_for_lda(sentence)
    print(f"Phrase: {keywords}") # TEMP - Debug

    # Generate query
    processed_keywords = []
    for keyword in keywords:
        processed_keywords.append(replace_suffix_with_wildcard(keyword))

    response = scripture.search(" ".join(processed_keywords), 3, "0") # Search

    print(f"Response:\n{json.dumps(response, indent = 4, sort_keys = True)}") # TEMP - Debug

    return {'count': len(response), 'response': response} # Result


if __name__ == '__main__':
    print("Starting app!")
    # app.run(debug=True) # TEMP - Debug
    app.run()
