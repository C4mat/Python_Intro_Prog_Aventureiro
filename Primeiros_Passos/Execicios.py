# EXERCICIOS
# 1 - Escreva um programa que leia o ano de nascimento do usuario e retorne quantos anos ele fará em 2035
# 2 - Escreva um programa que leia um numero digitado e retorne o seu antecessor e o seu sucessor. Vamos Considerar como antecessor o número inteiro imediatamente inferior ao numero digitado e como sucessor o inteiro imediatamente superior ao numero digitado
# 3 - Faça um programa que leia largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta - la, sabendo que em cada litro de tinta pinta uma area de 2 metros quadrados
# -------------------------------------------
# 1
# print("Programa para saber a sua idade em 2035 \n")
# idade = int( input("Digite o seu ano de nascimento: "))
# id = 2035 - idade
# print(f"Essa será a sua idade em 2035: {id}")
# --------------------------------------------------

# 2
# print("Programa para exibir o antecessor e sucessor de um numero digitado")
# num = int(input("Digite um numero inteiro: "))
# ant = num - 1
# suc = num + 1
# print(f"Esse é sucessor: {suc}")
# print(f"Esse é o antecessor: {ant}")

# 3
print("Programa para Calcular Area e quantidade de Tinta \n")
lar = int(input("Digite a Largura"))
alt = int(input("Digite a Altura"))
area = lar * alt
qtdt = area/2 