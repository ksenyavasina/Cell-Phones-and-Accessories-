import pandas as pd
import numpy as np
from collections import defaultdict
from gensim.models import word2vec
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from function_review_NLP import review_to_wordsentence
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time


model = word2vec.Word2Vec.load('plot_model')
w2v = dict(zip(model.wv.index2word, model.wv.syn0))

data = pd.read_csv('data.csv', delimiter=',')

df = data[data['review/score'] != 3]
X = df['review/text']
y_dict = {1:0, 2:0, 4:1, 5:1}
y = df['review/score'].map(y_dict)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

X_train = review_to_wordsentence(X_train)
X_test = review_to_wordsentence(X_test)

class tfidf_vectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.word2weight = None
        self.dim = len(next(iter(w2v.values())))

    def fit(self, X):
        tfidf = TfidfVectorizer(analyzer=lambda x: x)
        tfidf.fit(X)
        max_idf = max(tfidf.idf_)
        self.word2weight = defaultdict(
            lambda: max_idf,
            [(w, tfidf.idf_[i]) for w, i in tfidf.vocabulary_.items()])

        return self

    def transform(self, X):
        return np.array([
                np.mean([self.word2vec[w] * self.word2weight[w]
                         for w in words if w in self.word2vec] or
                        [np.zeros(self.dim)], axis=0)
                for words in X
            ])

X_train_tfidf=tfidf_vectorizer(w2v).fit(X_train).transform(X_train)
X_test_tfidf=tfidf_vectorizer(w2v).fit(X_test).transform(X_test)

def classification(clf_model):
    start_time = time.time()
    clf = clf_model
    clf.fit(X_train_tfidf, y_train)
    y_pred = clf.predict(X_test_tfidf)
    print('Testing accuracy %s' % accuracy_score(y_test, y_pred))
    print("--- %s seconds ---" % (time.time() - start_time))

classification(RandomForestClassifier(n_estimators=100))

classification(LogisticRegression())



