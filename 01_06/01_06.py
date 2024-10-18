import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

texto = "El procesamiento de lenguaje natural es fascinante. La inteligencia artificial y el aprendizaje automático son campos muy prometedores."

nltk.download('punkt')
nltk.download('stopwords')

palabras_tokenizadas = word_tokenize(texto.lower())
stop_words = set(stopwords.words('spanish'))
texto_filtrado = [palabra for palabra in palabras_tokenizadas if palabra.isalnum() and palabra not in stop_words]

vocabulario = set(texto_filtrado)
print("Vocabulario:", vocabulario)
print("Número de términos únicos:", len(vocabulario))