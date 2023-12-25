# Crie um jogo em que o programa escolhe um número aleatório e o jogador tenta adivinhar o número. Dê dicas ao jogador (maior ou menor) até que ele adivinhe corretamente.

import random

nAleatorio = random.randint(1, 20)  # Escolha um número aleatório entre 1 e 20

while True:
    n = int(input("Adivinhe o número aleatório que aparecerá entre 1 e 20: "))

    if n == nAleatorio:
        print(f"Parabéns! O número aleatório foi {nAleatorio}. Você acertou!")
        break  # Encerra o loop quando o jogador adivinhar corretamente
    else:
        if n < nAleatorio:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
