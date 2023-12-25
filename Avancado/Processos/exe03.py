''' Programação Concorrente com concurrent.futures e Processos:
Escreva um programa que utiliza a biblioteca concurrent.futures para realizar tarefas em paralelo usando processos em vez de threads. Compare o desempenho entre as duas abordagens.'''

import concurrent.futures
import time

def calcular_soma(lista):
    soma = sum(lista)
    return soma

if __name__ == "__main__":
    # Criar uma lista grande para cálculos
    lista_grande = list(range(1, 1000001))

    # Usar ProcessPoolExecutor para executar tarefas em paralelo usando processos
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Medir o tempo para tarefas usando processos
        inicio = time.time()
        resultados = [executor.submit(calcular_soma, lista_grande) for _ in range(5)]
        for resultado in concurrent.futures.as_completed(resultados):
            soma = resultado.result()
            print(f"Soma: {soma}")
        fim = time.time()
        print(f"Tempo total com processos: {fim - inicio} segundos")

    # Usar ThreadPoolExecutor para executar tarefas em paralelo usando threads (para comparação)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Medir o tempo para tarefas usando threads
        inicio = time.time()
        resultados = [executor.submit(calcular_soma, lista_grande) for _ in range(5)]
        for resultado in concurrent.futures.as_completed(resultados):
            soma = resultado.result()
            print(f"Soma: {soma}")
        fim = time.time()
        print(f"Tempo total com threads: {fim - inicio} segundos")
