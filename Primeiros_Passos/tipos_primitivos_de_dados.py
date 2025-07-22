# Tipos primitivos de dados em Python #
# Os tipos primitivos de dados são as categorias básicas de dados que podem ser manipulados em Python #


a = 1
type(a)  # Verifica o tipo da variavel a, que é um inteiro
print(type(a))  # Imprime o tipo da variavel a, que é um inteiro

f = "curso de python"  # A variavel f recebe uma string
print(type(f))  # Imprime o tipo da variavel f, que é uma string

g = 2.15  # A variavel g recebe um float
print(type(g))  # Imprime o tipo da variavel g, que é um float
complexo = 1j  # A variavel complexo recebe um numero complexo
print(type(complexo))  # Imprime o tipo da variavel complexo, que é um complexo

# Uma string é como uma caixinha onde guardamos palavras, frases ou qualquer texto. Por exemplo, quando você escreve seu nome no computador, ele vira uma string! Assim, o computador entende e pode mostrar as palavras para você.

palavra = "palavra"  # isso é uma string
print(palavra)
pov = """esse texto 
foi feito
 em 3 linhas de codigo"""
print(pov)

# agora os dados booleanos para comparação logica True e False
print(1 == 1)  # True
print(1 == 2)  # False
print(type(1 == 1))  # tipo bool
