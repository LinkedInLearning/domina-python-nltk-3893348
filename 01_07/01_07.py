import nltk
from nltk.tokenize import word_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

texto = "Carlos está aprendiendo sobre procesamiento de lenguaje natural."
