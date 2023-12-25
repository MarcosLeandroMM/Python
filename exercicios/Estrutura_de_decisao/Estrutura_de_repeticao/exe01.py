# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

while True:
    try:
        nota = int(input("Digite uma nota entre zero a dez: "))
        if 0 <= nota <= 10:
            break
        else:
            print("Digite um valor entre zero a dez.")
    except ValueError:
        ("Digite um valor válido")

print("A nota digita foi", nota)
