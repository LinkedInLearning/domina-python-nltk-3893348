import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

texto = "La nueva aplicación es rápida, intuitiva y fácil de usar."

nltk.download('punkt')

tokens = word_tokenize(texto)

bigramas = list(ngrams(tokens, 2))
trigramas = list(ngrams(tokens, 3))

print("Bigramas:", bigramas)
print("Trigramas:", trigramas)
