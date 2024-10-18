import nltk
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

with open('texto_espanol.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

tokens = word_tokenize(texto)

bigramas = nltk.bigrams(tokens)
frec_condicional = ConditionalFreqDist(bigramas)

def generar_texto(texto_semilla, numero_palabras=10):
    palabras = texto_semilla.split()
    for _ in range(numero_palabras):
        posibles_siguientes = list(frec_condicional[palabras[-1]].keys())
        probabilidades = list(frec_condicional[palabras[-1]].values())
        
        if posibles_siguientes:
            siguiente_palabra = random.choices(posibles_siguientes, probabilidades)[0]
            palabras.append(siguiente_palabra)
        else:
            break
    return ' '.join(palabras)

texto_generado = generar_texto("Ella estaba", 10)
print(texto_generado)
