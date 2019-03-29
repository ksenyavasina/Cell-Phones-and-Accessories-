import pandas as pd
import nltk.data
from gensim.models import word2vec
import logging
from function_review_NLP import review_to_sentences_list
import time

data = pd.read_csv('data.csv', delimiter=',')
reviews  = data['review/text']

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = []

print("Parsing sentences from plot set")
for review in reviews:
    sentences += review_to_sentences_list(review, tokenizer)


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
print("Go to make model")

start_time = time.time()
model = word2vec.Word2Vec(sentences, size=300, window=10, workers=4, sg = 1, sample=0.001, negative=10, min_count=10)

model.init_sims(replace=True)
model_name = "plot_model"
model.save(model_name)

print("--- %s seconds ---" % (time.time() - start_time))
