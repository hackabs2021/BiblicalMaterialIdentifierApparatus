import spacy
import nltk
import os

nltk.download('wordnet')
from nltk.corpus import wordnet as wn

spacy.load('en_core_web_sm')
from spacy.lang.en import English
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
import random
from gensim import corpora
import pandas as pd


class ScriptureAnalyzer:

    def __init(self, word=None):
        # print("do nothing") # TEMP - Debug
        self.dictionary = None
        self.text_data = []

    def tokenize(self, text):
        lda_tokens = []
        parser = English()
        tokens = parser(text)
        for token in tokens:
            if token.orth_.isspace():
                continue
            elif token.like_url:
                lda_tokens.append('URL')
            elif token.orth_.startswith('@'):
                lda_tokens.append('SCREEN_NAME')
            else:
                lda_tokens.append(token.lower_)
        return lda_tokens

    def get_lemma(self, word):
        lemma = wn.morphy(word)
        if lemma is None:
            return word
        else:
            return lemma

    def get_lemma2(self, word):
        return WordNetLemmatizer().lemmatize(word)

    def prepare_text_for_lda(self, text):
        tokens = self.tokenize(text)
        tokens = [token for token in tokens if len(token) > 4]
        tokens = [token for token in tokens if token not in en_stop]
        tokens = [self.get_lemma(token) for token in tokens]
        return tokens

    def put_in_text_data(self):
        # print("prepare text for lda and put in dictionary holder") # TEMP - Debug
        self.text_data = []
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))
        # print(CURR_DIR) # TEMP - Debug
        with open(CURR_DIR + '\\covid_broad-match_us_2021-10-23.csv') as f:
            for line in f:
                if random.random() > .99:
                    splitline = line.split(',')[0]
                    tokens = self.prepare_text_for_lda(splitline)
                    # #print(tokens) # TEMP - Debug
                    self.text_data.append(tokens)
        # df = pd.read_csv(r'uncertainty_phrase-match_us_2021-10-24.csv')
        # df['clean_keyword'] = df['keyword'].apply(lambda x: nltk.tokenize.word_tokenize(x))

    def find_10_topics(self):
        # print("find 10 topics") # TEMP - Debug
        dictionary = corpora.Dictionary(self.text_data)
        corpus = [dictionary.doc2bow(text) for text in self.text_data]
        import pickle
        pickle.dump(corpus, open('corpus.pkl', 'wb'))
        dictionary.save('dictionary.gensim')
        import gensim
        NUM_TOPICS = 10
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
        ldamodel.save('model5.gensim')

        # # TEMP- Debug
        # topics = ldamodel.print_topics(num_words=4)
        # print("starting topics:")
        # for topic in topics:
        #     print(topic)
        # print("***********************")

        #new_doc = "disease"
        #new_doc = self.prepare_text_for_lda(new_doc)
        #new_doc_bow = dictionary.doc2bow(new_doc)
        # #print(new_doc_bow) # TEMP - Debug
        # #print(ldamodel.get_document_topics(new_doc_bow)) # TEMP - Debug


if __name__ == '__main__':
    scripture = ScriptureAnalyzer()
    scripture.put_in_text_data()
    scripture.find_10_topics()
