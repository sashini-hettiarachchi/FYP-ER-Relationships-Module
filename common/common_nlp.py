import nltk
from nltk.corpus import stopwords
from utils.file_manipulation import input_text


stopWords = set(stopwords.words('english'))
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.PorterStemmer()

def text_into_sentence():
    nltk.sent_tokenize(input_text)
    return nltk.sent_tokenize(input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word

