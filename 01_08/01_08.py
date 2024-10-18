import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

texto = "John trabaja en LinkedIn desde el 2025"
