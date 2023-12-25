# Avançado - Classificação de Lista: Escreva um programa que ordene uma lista de números inseridos pelo usuário em ordem crescente ou decrescente, dependendo da escolha do usuário.

# Função para classificar a lista em ordem crescente
def ordenar_crescente(lista):
    return sorted(lista)

# Função para classificar a lista em ordem decrescente
def ordenar_decrescente(lista):
    return sorted(lista, reverse=True)

# Solicita ao usuário uma lista de números separados por espaços
entrada = input("Digite uma lista de números separados por espaços: ")

# Converte a entrada do usuário em uma lista de números
numeros = [float(numero) for numero in entrada.split()]

# Pergunta ao usuário se deseja ordenar em ordem crescente ou decrescente
ordem = input("Deseja ordenar em ordem crescente (C) ou decrescente (D)? ").upper()

# Verifica a escolha do usuário e ordena a lista
if ordem == 'C':
    lista_ordenada = ordenar_crescente(numeros)
elif ordem == 'D':
    lista_ordenada = ordenar_decrescente(numeros)
else:
    print("Escolha inválida. Por favor, digite 'C' para ordem crescente ou 'D' para ordem decrescente.")
    lista_ordenada = None

# Imprime a lista ordenada, se houver
if lista_ordenada:
    print("Lista ordenada:", lista_ordenada)
