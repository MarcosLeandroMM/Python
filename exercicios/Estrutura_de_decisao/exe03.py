# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = input("Digite F se feminino e M se masculino: ")
if letra == 'M':
    print("Sexo masculino!")
elif letra == 'F':
    print("Sexo feminino!")
else:
    print("Sexo inválido!")