'''
Multiprocessamento Simples:
Crie um programa que execute várias tarefas em processos separados usando a biblioteca multiprocessing. Compare o desempenho da execução multithreaded com a execução multiprocessada.

'''
import multiprocessing
import threading
import time

def calcular_soma(lista):
    soma = sum(lista)
    print(f"Soma: {soma}")

def tarefa_multiprocessada(lista):
    processo = multiprocessing.Process(target=calcular_soma, args=(lista,))
    processo.start()
    processo.join()

def tarefa_multithreaded(lista):
    thread = threading.Thread(target=calcular_soma, args=(lista,))
    thread.start()
    thread.join()

if __name__ == "__main__":
    # Criar uma lista grande para cálculos
    lista_grande = list(range(1, 1000001))

    # Executar tarefa usando multiprocessing
    inicio = time.time()
    for _ in range(5):
        tarefa_multiprocessada(lista_grande)
    fim = time.time()
    print(f"Tempo total com multiprocessing: {fim - inicio} segundos")

    # Executar tarefa usando multithreading
    inicio = time.time()
    for _ in range(5):
        tarefa_multithreaded(lista_grande)
    fim = time.time()
    print(f"Tempo total com multithreading: {fim - inicio} segundos")

'''
Neste exemplo, a função calcular_soma realiza uma tarefa simples de somar os elementos de uma lista. As funções tarefa_multiprocessada e tarefa_multithreaded criam processos ou threads para executar essa tarefa, respectivamente. O tempo total para realizar a tarefa é medido para ambos os casos, e você pode comparar os tempos de execução.

Note que o GIL (Global Interpreter Lock) em Python limita a execução de threads em paralelo, tornando a execução multithreaded não tão eficaz para certos tipos de tarefas. Em contrapartida, a execução multiprocessada geralmente oferece melhor desempenho para tarefas intensivas em CPU, pois cada processo tem seu próprio interpretador Python e, portanto, pode executar em paralelo em CPUs multi-core.

'''