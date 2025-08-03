from gramatica import Gramatica
from simplificacao import *
from chomsky import para_chomsky
from greibach import para_greibach
from melhorias import *

entrada = [
    "S -> aAa | bBv",
    "A -> a | aA"
]

g = Gramatica(entrada)
print("Original:\n", g)

remover_simbolos_inuteis(g)
remover_producoes_vazias(g)
substituir_producoes_unitarias(g)
print("\nApós Simplificação:\n", g)

fatorar_esquerda(g)
remover_recursao_esquerda(g)
print("\nApós Melhorias:\n", g)

para_chomsky(g)
print("\nForma Normal de Chomsky:\n", g)

para_greibach(g)
