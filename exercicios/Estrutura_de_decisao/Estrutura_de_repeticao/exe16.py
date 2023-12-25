# Avançado - Jogo de Forca: Crie um jogo de forca onde o jogador deve adivinhar uma palavra oculta. O jogo deve mostrar o progresso e o número de tentativas restantes.

import random

# Lista de palavras para o jogo
palavras = ["python", "javascript", "java", "html", "css", "ruby", "php", "csharp", "typescript", "swift"]

# Escolha aleatoriamente uma palavra da lista
palavra_oculta = random.choice(palavras)

# Inicialização de variáveis
tamanho_palavra = len(palavra_oculta)
letras_certas = []
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")
print(f"A palavra tem {tamanho_palavra} letras.")
print("_ " * tamanho_palavra)

while True:
    letra = input("\nDigite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra válida.")
        continue

    if letra in letras_certas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra_oculta:
        letras_certas.append(letra)
        print(f"Letra '{letra}' está na palavra!")

        progresso = ""
        for letra_palavra in palavra_oculta:
            if letra_palavra in letras_certas:
                progresso += letra_palavra + " "
            else:
                progresso += "_ "
        
        print(progresso)

        if set(letras_certas) == set(palavra_oculta):
            print("\nParabéns! Você venceu!")
            break
    else:
        tentativas -= 1
        print(f"Letra '{letra}' não está na palavra.")
        print(f"Tentativas restantes: {tentativas}")

        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra_oculta)
            break
