"""
Assincronia e concorrência são conceitos importantes em programação que permitem que você lide com tarefas assíncronas e paralelas de forma eficiente em Python. Vou explicar esses conceitos e fornecer exemplos para ilustrar o uso de asyncio, threads e processos em Python.

Assincronia:

A assincronia se refere à capacidade de executar tarefas em paralelo sem bloquear o programa principal. Isso é útil quando você precisa lidar com operações de E/S (entrada/saída) que podem ser demoradas, como solicitações de rede, leitura/gravação de arquivos, etc. Em Python, você pode usar a biblioteca asyncio para lidar com tarefas assíncronas.

Exemplo usando asyncio:
"""

import asyncio

async def tarefa_assincrona(nome):
    await asyncio.sleep(1)
    print(f"Executando tarefa assíncrona {nome}")

async def main():
    tarefas = [tarefa_assincrona("A"), tarefa_assincrona("B")]
    await asyncio.gather(*tarefas)

if __name__ == "__main__":
    asyncio.run(main())

"""
Neste exemplo, duas tarefas assíncronas são definidas com async def. O await asyncio.sleep(1) simula uma operação de E/S demorada. await asyncio.gather(*tarefas) é usado para executar as tarefas em paralelo.
"""

"""
Concorrência:

Concorrência envolve a execução simultânea de várias tarefas em paralelo. Python oferece suporte a concorrência usando threads e processos.

Threads: As threads permitem que partes do código sejam executadas simultaneamente. O módulo threading é usado para trabalhar com threads em Python.
Exemplo usando threads:
"""

import threading

def tarefa(nome):
    for _ in range(3):
        print(f"Executando tarefa {nome}")

tarefa1 = threading.Thread(target=tarefa, args=("A",))
tarefa2 = threading.Thread(target=tarefa, args=("B",))

tarefa1.start()
tarefa2.start()

tarefa1.join()
tarefa2.join()

# Neste exemplo, duas threads são criadas para executar a função tarefa em paralelo.

""" Processos: Os processos permitem que você execute partes do código em processos separados, permitindo paralelismo real. O módulo multiprocessing é usado para trabalhar com processos em Python.
Exemplo usando processos:"""

import multiprocessing

def tarefa(nome):
    for _ in range(3):
        print(f"Executando tarefa {nome}")

if __name__ == "__main__":
    processo1 = multiprocessing.Process(target=tarefa, args=("A",))
    processo2 = multiprocessing.Process(target=tarefa, args=("B",))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

"""
Em Python, o uso do sublinhado simples _ como uma variável é uma convenção comum para representar um valor descartado ou uma variável que não será usada. É frequentemente usado em situações onde é necessário declarar uma variável, mas seu valor é insignificante ou não será utilizado. É uma maneira de indicar de forma clara e explícita que você não está interessado no valor da variável.
"""