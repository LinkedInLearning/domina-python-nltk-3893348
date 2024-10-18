import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
import ssl
from nltk.corpus import cess_esp

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')
nltk.download('cess_esp')

texto = "ESTE texot tienee algunos errrores de ortografia. Debería SER corregido correctamnete."
palabras_correctas = list(set(cess_esp.words()))
