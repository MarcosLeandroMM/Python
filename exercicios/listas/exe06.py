# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

# Crie uma lista para armazenar as médias dos alunos
medias = []

# Use um loop para coletar as notas dos 10 alunos
for aluno in range(10):
    notas = []
    for nota_numero in range(4):
        nota = float(input(f"Digite a {nota_numero+1}ª nota do aluno {aluno+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

# Use outro loop para contar o número de alunos com média maior ou igual a 7.0
alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        alunos_aprovados += 1

# Imprima as médias e o número de alunos aprovados
print("Médias dos alunos:")
for i, media in enumerate(medias, start=1):
    print(f"Aluno {i}: {media:.2f}")
    
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

    
    
    
    

