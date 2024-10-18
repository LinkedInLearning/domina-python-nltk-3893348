import nltk
from nltk import CFG
from nltk.parse import ChartParser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

gramatica = CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'Ella'
    VP -> V NP | VP PP
    Det -> 'un' | 'la'
    N -> 'gato' | 'mesa'
    V -> 'encontro'
    P -> 'bajo'
""")

analizador = ChartParser(gramatica)

oracion = 'Ella encontro un gato bajo la mesa'.split()

arboles = list(analizador.parse(oracion))

if arboles:
    for arbol in arboles:
        print(arbol) 
        print("Árbol en formato estructurado:")
        arbol.pretty_print()  
        print("Mostrando el árbol gráficamente:")
        arbol.draw()
else:
    print("No se encontró ningún análisis sintáctico válido para la oración.")