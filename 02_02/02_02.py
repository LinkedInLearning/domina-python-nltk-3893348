import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

texto = "La nueva aplicación es rápida, intuitiva y fácil de usar. La aplicación es muy útil y rápida."

nltk.download('punkt')
