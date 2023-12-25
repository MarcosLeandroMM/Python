# Intermediário - Adivinhe o número: Crie um jogo onde o computador gera um número aleatório e o jogador deve adivinhar qual é o número. O jogo deve fornecer dicas se o palpite for muito alto ou muito baixo.

import random

# Gere um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Número de tentativas permitidas
tentativas_maximas = 10
tentativas = 0

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número secreto entre 1 e 100.")

while tentativas < tentativas_maximas:
    # Solicite um palpite ao jogador
    palpite = int(input("Digite seu palpite: "))
    
    # Atualize o número de tentativas
    tentativas += 1
    
    # Verifique se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Tente um número mais alto.")
    else:
        print("Tente um número mais baixo.")

# Se o jogador não adivinhar o número após o número máximo de tentativas
if tentativas == tentativas_maximas:
    print(f"Você esgotou todas as {tentativas_maximas} tentativas. O número secreto era {numero_secreto}. O jogo acabou.")
