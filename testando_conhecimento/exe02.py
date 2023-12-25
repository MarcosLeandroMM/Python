#  Escreva uma função que recebe uma lista de números e retorna uma lista com os números em ordem inversa.

def list_number(lista):
    lista = [float(numero) for numero in lista.split(",")]
    lista_invertida = lista[::-1]
    return lista_invertida
    


lista_de_numeros = input("Digite uma lista de números separadas por vírgulas: ")

ordem_inversa = list_number(lista_de_numeros)

print(f"A ordem inversa da lista é {ordem_inversa} ")