# Notas dos Alunos

por = float(input("Digite a nota de portugues do aluno: "))
mat = float(input("Digite a nota de matematica do aluno: "))
hist = float(input("Digite a nota de historia do aluno: "))
geo = float (input("Digite a nota de geografia do aluno: "))
soma = por + mat + hist + geo
med = soma/4

print (f'''essas são as notas do aluno
   portugues: {por}
   Matematica{mat} 
   Historia {hist} 
   Geografia {geo} ''')
print (f"essa é a media do aluno: {med}")
