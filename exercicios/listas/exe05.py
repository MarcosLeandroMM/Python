

# Crie uma lista vazia para armazenar os números
numeros = []

# Crie duas listas separadas para números pares e ímpares
pares = []
impares = []

# Use um loop para ler os números do usuário
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
    # Verifique se o número é par ou ímpar e adicione-o à lista apropriada
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Agora, as listas 'numeros', 'pares' e 'impares' contêm os números fornecidos pelo usuário

print(f"Os números da lista são: {', '.join(map(str, numeros))}")
print(f"Os números pares são: {', '.join(map(str, pares))}")
print(f"Os números ímpares são: {', '.join(map(str, impares))}")
