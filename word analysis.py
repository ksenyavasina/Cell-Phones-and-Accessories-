import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('data.csv', delimiter=',')
df = data[data['review/score'] != 3]
X = df['review/text']
y_dict = {1:0, 2:0, 4:1, 5:1}
y = df['review/score'].map(y_dict)


def word_analysis(X, y, model, clf_model):
    X_m = model.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_m, y, random_state=0)
    clf = clf_model.fit(X_train, y_train)
    ACU = clf.score(X_test, y_test)
    print('Model Accuracy: {}'.format(ACU))

    w = model.get_feature_names()
    coef = clf.coef_.tolist()[0]
    coeff_df = pd.DataFrame({'Word': w, 'Coefficient': coef})
    coeff_df = coeff_df.sort_values(['Coefficient', 'Word'], ascending=[0, 1])
    print('')
    print('-Top 20 positive-')
    print(coeff_df.head(20).to_string(index=False))
    print('')
    print('-Top 20 negative-')
    print(coeff_df.tail(20).to_string(index=False))



c = CountVectorizer(stop_words='english')
tfidf = TfidfVectorizer(stop_words = 'english')
word_analysis(X, y, tfidf, LogisticRegression())
