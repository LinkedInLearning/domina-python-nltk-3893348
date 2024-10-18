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

def normalizar_texto(texto):
    texto_minusculas = texto.lower()
    palabras_tokenizadas = nltk.word_tokenize(texto_minusculas)
    palabras_sin_puntuacion = [palabra for palabra in palabras_tokenizadas if palabra.isalnum()]
    return ' '.join(palabras_sin_puntuacion)

def corregir_ortografia_jaccard(texto):
    palabras = nltk.word_tokenize(texto)
    palabras_corregidas = []
    
    for palabra in palabras:
        if len(palabra) < 3:
            palabras_corregidas.append(palabra)
            continue
        
        trigramas_palabra = set(ngrams(palabra, 3))
        
        posibles_correcciones = [(jaccard_distance(trigramas_palabra, set(ngrams(w, 3))), w)
                                 for w in palabras_correctas if len(w) >= 3 and w[0] == palabra[0] and abs(len(w) - len(palabra)) <= 2]
        
        if posibles_correcciones:
            correccion = sorted(posibles_correcciones, key=lambda val: val[0])[0][1]
            palabras_corregidas.append(correccion)
        else:
            palabras_corregidas.append(palabra)
    
    return ' '.join(palabras_corregidas)

texto_normalizado = normalizar_texto(texto)
texto_corregido = corregir_ortografia_jaccard(texto_normalizado)

print("Texto original:", texto)
print("Texto normalizado:", texto_normalizado)
print("Texto corregido:", texto_corregido)
