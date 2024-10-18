import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

texto = "John trabaja en LinkedIn desde el 2025"

nltk.download('punkt')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

palabras_tokenizadas = word_tokenize(texto)
pos_tags = nltk.pos_tag(palabras_tokenizadas)
nombre_entidades = ne_chunk(pos_tags)

print(nombre_entidades)
