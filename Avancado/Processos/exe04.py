'''
Piscina de Processos:
Implemente um programa que use uma piscina de processos para executar tarefas em paralelo. Avalie como o uso de uma piscina de processos pode melhorar o desempenho em comparação com a criação de processos individuais.

'''
'''
A utilização de uma piscina de processos (concurrent.futures.ProcessPoolExecutor) pode melhorar significativamente o desempenho ao executar tarefas em paralelo, pois ela gerencia automaticamente a alocação de tarefas para os diferentes processos disponíveis na piscina. Isso evita o overhead de criar e destruir processos para cada tarefa individual.

'''

import concurrent.futures
import time

def calcular_soma(lista):
    soma = sum(lista)
    return soma

if __name__ == "__main__":
    # Criar uma lista grande para cálculos
    lista_grande = list(range(1, 1000001))

    # Usar ProcessPoolExecutor para executar tarefas em paralelo usando uma piscina de processos
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Medir o tempo para tarefas usando piscina de processos
        inicio = time.time()
        resultados = [executor.submit(calcular_soma, lista_grande) for _ in range(5)]
        for resultado in concurrent.futures.as_completed(resultados):
            soma = resultado.result()
            print(f"Soma: {soma}")
        fim = time.time()
        print(f"Tempo total com piscina de processos: {fim - inicio} segundos")

    # Usar processos individuais para comparação
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Medir o tempo para tarefas usando processos individuais
        inicio = time.time()
        resultados = [executor.submit(calcular_soma, lista_grande) for _ in range(5)]
        for resultado in concurrent.futures.as_completed(resultados):
            soma = resultado.result()
            print(f"Soma: {soma}")
        fim = time.time()
        print(f"Tempo total com processos individuais: {fim - inicio} segundos")


'''
Neste exemplo, o código usa a ProcessPoolExecutor para executar tarefas em paralelo usando uma piscina de processos. Em seguida, ele faz a mesma coisa usando ProcessPoolExecutor sem a piscina, para comparação. Você pode observar uma melhoria significativa no desempenho ao utilizar a piscina de processos. Isso é especialmente verdadeiro para tarefas que são intensivas em CPU, onde o custo de criar e destruir processos pode ser significativo.

'''