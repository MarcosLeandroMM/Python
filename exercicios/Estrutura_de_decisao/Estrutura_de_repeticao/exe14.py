# Avançado - Criptografia de Cifra de César: Implemente um programa que criptografe uma mensagem usando a Cifra de César. Peça ao usuário para fornecer uma mensagem e um valor de deslocamento e, em seguida, cifre a mensagem.

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            maiuscula = char.isupper()  # Verifica se é letra maiúscula
            char = char.lower()  # Converte para minúscula para facilitar a cifra
            codigo = ord(char) - ord('a')  # Obtém o código da letra 'a' como base (0-25)
            codigo_cifrado = (codigo + deslocamento) % 26  # Aplica o deslocamento
            char_cifrado = chr(codigo_cifrado + ord('a'))  # Converte de volta para caractere
            if maiuscula:
                char_cifrado = char_cifrado.upper()  # Se a letra original era maiúscula, mantenha-a maiúscula
            resultado += char_cifrado
        else:
            resultado += char  # Se não for uma letra, mantenha o caractere original
    
    return resultado

# Solicita ao usuário a mensagem e o valor de deslocamento
mensagem = input("Digite a mensagem que você deseja criptografar: ")
deslocamento = int(input("Digite o valor de deslocamento (um número inteiro): "))

mensagem_cifrada = cifra_de_cesar(mensagem, deslocamento)

print("Mensagem cifrada:", mensagem_cifrada)
