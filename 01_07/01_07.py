import nltk
from nltk.tokenize import word_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

texto = "Carlos está aprendiendo sobre procesamiento de lenguaje natural."

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

palabras_tokenizadas = word_tokenize(texto)
pos_tags = nltk.pos_tag(palabras_tokenizadas)

print(pos_tags)
