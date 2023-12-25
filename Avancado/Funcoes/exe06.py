'''

Cálculo de Área de Formas Geométricas:
Escreva funções para calcular a área de diferentes formas geométricas, como círculos, triângulos e retângulos. Use funções anônimas (lambda) para calcular a área com base em argumentos fornecidos.
'''

# Função para calcular a área de um círculo
area_do_circulo = lambda raio: 3.14159 * raio ** 2

# Função para calcular a área de um triângulo
area_do_triangulo = lambda base, altura: 0.5 * base * altura

# Função para calcular a área de um retângulo
area_do_retangulo = lambda comprimento, largura: comprimento * largura

# Exemplo de uso:
raio = 5
base = 4
altura = 6
comprimento = 7
largura = 3

area_circulo = area_do_circulo(raio)
area_triangulo = area_do_triangulo(base, altura)
area_retangulo = area_do_retangulo(comprimento, largura)

print(f"Área do círculo com raio {raio}: {area_circulo:.2f}")
print(f"Área do triângulo com base {base} e altura {altura}: {area_triangulo:.2f}")
print(f"Área do retângulo com comprimento {comprimento} e largura {largura}: {area_retangulo:.2f}")
