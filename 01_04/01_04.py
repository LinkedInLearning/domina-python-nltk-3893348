from nltk.stem import SnowballStemmer

texto = ["jugando", "jugador", "jugarán", "juego"]

stemmer = SnowballStemmer('spanish')

palabras_stems = [stemmer.stem(palabra) for palabra in texto]
print(palabras_stems)
