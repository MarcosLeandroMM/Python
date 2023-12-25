# Avançado - Calculadora com Menu: Implemente uma calculadora que permite ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação, divisão) em um menu. O programa deve continuar a pedir operações até que o usuário decida sair.


# Função para realizar a operação de adição
def adicao(x, y):
    return x + y

# Função para realizar a operação de subtração
def subtracao(x, y):
    return x - y

# Função para realizar a operação de multiplicação
def multiplicacao(x, y):
    return x * y

# Função para realizar a operação de divisão
def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

while True:
    # Menu de operações
    print("\nEscolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = input("Digite o número da operação desejada: ")

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha not in ('1', '2', '3', '4'):
        print("Escolha inválida. Por favor, escolha uma opção válida.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = adicao(num1, num2)
        print("Resultado:", resultado)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
        print("Resultado:", resultado)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
        print("Resultado:", resultado)
    elif escolha == '4':
        resultado = divisao(num1, num2)
        print("Resultado:", resultado)
