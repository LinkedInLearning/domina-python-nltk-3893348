import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

texto = "Este producto me encanta y funciona de maravilla, aunque en ocasiones se apaga por sí solo. ¿Tienen alguna idea de por qué sucede?"

palabras_tokens = word_tokenize(texto)
print("Tokenización de palabras:", palabras_tokens)

oraciones_tokens = sent_tokenize(texto)
print("Tokenización de oraciones:", oraciones_tokens)

personalizada_tokens = regexp_tokenize(texto, r'\b[a-zA-Z]+\b')
print("Tokenización personalizada:", personalizada_tokens)
