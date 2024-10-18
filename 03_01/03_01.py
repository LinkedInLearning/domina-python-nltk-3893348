import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')
nltk.download('stopwords')

textos = {
    "es": "El procesamiento de lenguaje natural es fascinante.",
    "en": "Natural language processing is fascinating.",
    "fr": "Le traitement du langage naturel est fascinant."
}