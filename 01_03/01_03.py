import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
texto = ["running", "ran", "runs"]

nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

lemmas = [lemmatizer.lemmatize(palabra, wordnet.VERB) for palabra in texto]
print(lemmas)
