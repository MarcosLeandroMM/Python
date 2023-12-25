'''
Compartilhamento de Dados entre Processos:
Crie um programa que compartilhe dados entre processos usando estruturas de dados compartilhadas, como multiprocessing.Array ou multiprocessing.Value. Certifique-se de lidar com a sincronização apropriada dos dados compartilhados.


'''

'''

A biblioteca multiprocessing em Python fornece algumas estruturas de dados compartilhadas, como multiprocessing.Array e multiprocessing.Value, que podem ser utilizadas para compartilhar dados entre processos. Aqui está um exemplo simples que usa multiprocessing.Array para compartilhar uma lista entre processos, e utiliza semáforos para garantir sincronização adequada:

'''

import multiprocessing
import time

def calcular_soma_compartilhada(i, array_compartilhado, semaforo):
    # Seção crítica - usar semáforo para garantir acesso exclusivo ao array compartilhado
    with semaforo:
        for j in range(len(array_compartilhado)):
            array_compartilhado[j] += i

if __name__ == "__main__":
    # Criar um array compartilhado e inicializá-lo com zeros
    tamanho_array = 10
    array_compartilhado = multiprocessing.Array('i', tamanho_array)
    array_compartilhado[:] = [0] * tamanho_array

    # Criar um semáforo para sincronizar o acesso ao array compartilhado
    semaforo = multiprocessing.Semaphore()

    # Criar processos para calcular a soma compartilhada
    processos = []
    for i in range(1, 6):
        processo = multiprocessing.Process(target=calcular_soma_compartilhada, args=(i, array_compartilhado, semaforo))
        processos.append(processo)

    # Iniciar os processos
    for processo in processos:
        processo.start()

    # Aguardar a conclusão dos processos
    for processo in processos:
        processo.join()

    # Exibir o resultado
    resultado_final = list(array_compartilhado)
    print(f"Resultado final: {resultado_final}")
