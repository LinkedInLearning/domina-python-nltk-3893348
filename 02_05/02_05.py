import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('vader_lexicon')

texto = "I love this app, it is very easy to use and fast. However, it sometimes freezes."

analizador = SentimentIntensityAnalyzer()
puntuacion = analizador.polarity_scores(texto)

print(puntuacion)
