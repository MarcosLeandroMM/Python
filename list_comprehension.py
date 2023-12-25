# Gerar uma lista de números pares de 0 a 10:
pares = [x for x in range(11) if x % 2 == 0]
print(pares)

# Elevar ao quadrado os números de 0 a 5:
quadrados = [x ** 2 for x in range(6)]
print(quadrados)

# Filtrar uma lista de palavras para aquelas que têm mais de 4 letras:
palavras = ["python", "é", "uma", "linguagem", "incrível"]
longas = [palavra for palavra in palavras if len(palavra) > 4]
print(longas)

# Gerar uma lista de tuplas representando coordenadas (x, y) para uma grade 3x3:
grade = [(x, y) for x in range(3) for y in range(3)]
print(grade)

# Converter uma lista de números em uma lista de strings:
numeros = [1, 2, 3, 4, 5]
strings = [str(num) for num in numeros]
print(strings)