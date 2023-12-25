# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def oneArgument(a):
    if a <= 0:
        return 'N'
    elif a >= 0:
        return 'P'
    
valor_a_definir = int(input("Digite um número inteiro: "))
funcao_aplicada = oneArgument(valor_a_definir)
print(f"Dado 'N' para 0 e negativo e 'P' para positivo, o número digitado é {funcao_aplicada}")
