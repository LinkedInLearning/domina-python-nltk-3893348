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

for idioma, texto in textos.items():
    tokens = word_tokenize(texto, language='spanish' if idioma == 'es' else 'english')
    
    if idioma == 'es':
        palabras_vacias = set(stopwords.words('spanish'))
    elif idioma == 'fr':
        palabras_vacias = set(stopwords.words('french'))
    else:
        palabras_vacias = set(stopwords.words('english'))
    
    tokens_filtrados = [palabra for palabra in tokens if palabra.isalnum() and palabra not in palabras_vacias]
    
    print(f"Texto en {idioma}:")
    print("Tokens filtrados:", tokens_filtrados)
