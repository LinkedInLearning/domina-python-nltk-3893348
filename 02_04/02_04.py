import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

documentos = [
    "La nueva aplicación es rápida e intuitiva.",
    "Esta aplicación es muy fácil de usar.",
    "Me encanta la interfaz rápida de la aplicación."
]