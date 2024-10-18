import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
texto = "Este es un ejemplo de análisis de sentimientos donde todos los usuarios se encuentran felices"

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('spanish'))
palabras_tokenizadas = word_tokenize(texto)


texto_filtrado = [palabra for palabra in palabras_tokenizadas if palabra.lower() not in stop_words]
print(texto_filtrado)
