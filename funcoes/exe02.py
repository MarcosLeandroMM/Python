def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join([str(j) for j in range(1, i + 1)])
        print(linha)

try:
    n = int(input("Digite o valor de n: "))
    imprimir_padrao(n)
except ValueError:
    print("Por favor, digite um número inteiro válido.")