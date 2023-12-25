'''
Cálculo de Área de Formas Geométricas:
Escreva funções para calcular a área de diferentes formas geométricas, como círculos, triângulos e retângulos. Use funções anônimas (lambda) para calcular a área com base em argumentos fornecidos.

'''


# Função para calcular a área de um círculo
circle_area = lambda radius: 3.14159 * radius ** 2

# Função para calcular a área de um triângulo
triangle_area = lambda base, height: 0.5 * base * height

# Função para calcular a área de um retângulo
rectangle_area = lambda length, width: length * width

# Exemplo de uso:
radius = 5
base = 4
height = 6
length = 7
width = 3

area_of_circle = circle_area(radius)
area_of_triangle = triangle_area(base, height)
area_of_rectangle = rectangle_area(length, width)

print(f"Área do círculo com raio {radius}: {area_of_circle:.2f}")
print(f"Área do triângulo com base {base} e altura {height}: {area_of_triangle:.2f}")
print(f"Área do retângulo com comprimento {length} e largura {width}: {area_of_rectangle:.2f}")
