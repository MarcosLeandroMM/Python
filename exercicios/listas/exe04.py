# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'x', 'z']

# Inicialize uma variável para contar as consoantes
contagem_consoantes = 0
consoantes_encontradas = []

# Itere sobre o vetor
for letra in vetor:
    # Verifique se a letra está na lista de consoantes
    if letra in consoantes:
        consoantes_encontradas.append(letra)
        contagem_consoantes += 1

print(f"As consoantes presentes no vetor são: {', '.join(consoantes_encontradas)}")
print(f"A quantidade de consoantes é: {contagem_consoantes}")
