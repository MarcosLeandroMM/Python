# Função lambda que soma dois números:
add = lambda x, y: x + y
print(add(5, 3))  # Saída: 8


# Função lambda que retorna o quadrado de um número:
square = lambda x: x ** 2
print(square(4)) 

# Função lambda que verifica se um número é par:
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Saída: True
print(is_even(7))  # Saída: False

# Função lambda que inverte uma string:
reverse_string = lambda s: s[::-1]
print(reverse_string("Python"))  # Saída: "nohtyP"

# Função lambda que ordena uma lista de números:
numbers = [5, 2, 9, 1, 6]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)  # Saída: [1, 2, 5, 6, 9]

# Função lambda usada com a função map para elevar cada elemento de uma lista ao quadrado:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Saída: [1, 4, 9, 16, 25]

# Função lambda usada com a função filter para filtrar números pares de uma lista:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Saída: [2, 4, 6, 8]