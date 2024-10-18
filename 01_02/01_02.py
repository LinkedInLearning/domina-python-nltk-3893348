import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
texto = "Este es un ejemplo de análisis de sentimientos donde todos los usuarios se encuentran felices"
