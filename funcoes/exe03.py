# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def threeArgument(a,b,c):
    soma = a + b + c
    return soma


try:
  primeiro_valor = int(input("Digite um número inteiro: "))
  segundo_valor = int(input("Digite um segundo valor: "))
  terceiro_valor = int(input("Digite um terceiro valor: "))
except:
   ValueError("Digite um número inteiro válido!")

funcao_aplicada = threeArgument(primeiro_valor, segundo_valor, terceiro_valor)
print(f"A soma dos três número é: ", funcao_aplicada)