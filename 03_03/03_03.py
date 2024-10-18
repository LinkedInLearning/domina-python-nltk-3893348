import nltk
from nltk.parse import DependencyGraph

datos_treebank = """
1   Juan    _   NNP _   _   2   NMOD    _   _
2   Pérez   _   NNP _   _   8   SUB     _   _
3   ,       _   ,   _   _   2   P       _   _
4   40      _   CD  _   _   5   NMOD    _   _
5   años    _   NNS _   _   6   AMOD    _   _
6   de      _   IN  _   _   2   NMOD    _   _
7   edad    _   NN  _   _   2   NMOD    _   _
8   asistirá _   VB  _   _   0   ROOT    _   _
9   a       _   IN  _   _   11  VMOD    _   _
10  la      _   DT  _   _   11  NMOD    _   _
11  reunión _   NN  _   _   8   OBJ     _   _
12  el      _   DT  _   _   15  NMOD    _   _
13  15      _   CD  _   _   15  NMOD    _   _
14  de      _   IN  _   _   15  NMOD    _   _
15  marzo   _   NNP _   _   11  VMOD    _   _
16  .       _   .   _   _   8   PUNCT   _   _
"""

grafo = DependencyGraph(datos_treebank)
grafo.tree().pprint()

for nodo_principal, relacion, dependiente in grafo.triples():
    print('({h[0]}, {h[1]}), {r}, ({d[0]}, {d[1]})'.format(h=nodo_principal, r=relacion, d=dependiente))
