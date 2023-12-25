# Intermediário - Sequência de Fibonacci: Escreva um programa que gere os primeiros 20 termos da sequência de Fibonacci.

# Número de termos desejados
n = 20

# Inicializando os primeiros dois termos
termo1 = 0
termo2 = 1

# Imprimindo os primeiros dois termos (0 e 1)
print(termo1)
print(termo2)

# Gerando os próximos termos da sequência
for _ in range(2, n):
    proximo_termo = termo1 + termo2
    print(proximo_termo)
    
    # Atualizando os termos anteriores
    termo1 = termo2
    termo2 = proximo_termo
