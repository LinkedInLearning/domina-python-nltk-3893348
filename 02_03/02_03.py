import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

texto = "La inteligencia artificial está revolucionando el mundo. La inteligencia artificial está presente en muchas áreas de nuestras vidas."

tokens = word_tokenize(texto)
frecuencia_palabras = Counter(tokens)

print(frecuencia_palabras.most_common(5))
