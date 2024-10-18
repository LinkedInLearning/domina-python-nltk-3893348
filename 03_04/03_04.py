import nltk
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

with open('texto_espanol.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

tokens = word_tokenize(texto)
