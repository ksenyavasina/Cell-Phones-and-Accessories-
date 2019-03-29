import re
from nltk.corpus import stopwords


def review_to_wordlist(plots):

    review_text = re.sub("[^a-zA-Z]", " ", plots)
    words = review_text.lower().split()
    stops = set(stopwords.words("english"))
    words = [w for w in words if not w in stops]

    return words


def review_to_sentences_list(plots, tokenizer):

    raw_sentences = tokenizer.tokenize(plots.strip())
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append(review_to_wordlist(raw_sentence))

    return sentences


def review_to_wordsentence(reviews):
    l = list()
    for review in reviews:
        review_text = re.sub("[^a-zA-Z]", " ", review)
        words = review_text.lower().split()
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
        l.append(words)

    return l