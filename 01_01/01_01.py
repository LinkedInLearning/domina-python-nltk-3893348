import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

texto = "Este producto me encanta y funciona de maravilla, aunque en ocasiones se apaga por sí solo. ¿Tienen alguna idea de por qué sucede?"
