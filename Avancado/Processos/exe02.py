'''
Comunicação entre Processos:
Implemente um programa que use processos para realizar cálculos em paralelo e demonstre a comunicação entre os processos por meio de pipes, filas ou outros mecanismos de IPC (Inter-Process Communication).

'''
import multiprocessing

def calcular_quadrado(numero, pipe):
    resultado = numero * numero
    pipe.send(resultado)
    pipe.close()

def calcular_cubo(numero, pipe):
    resultado = numero * numero * numero
    pipe.send(resultado)
    pipe.close()

if __name__ == "__main__":
    # Criação de pipes para comunicação entre processos
    pipe_quadrado, pipe_cubo = multiprocessing.Pipe()

    # Valores para cálculo
    valor = 5

    # Criando processos para calcular quadrado e cubo em paralelo
    processo_quadrado = multiprocessing.Process(target=calcular_quadrado, args=(valor, pipe_quadrado))
    processo_cubo = multiprocessing.Process(target=calcular_cubo, args=(valor, pipe_cubo))

    # Inicia os processos
    processo_quadrado.start()
    processo_cubo.start()

    # Aguarda a conclusão dos processos
    processo_quadrado.join()
    processo_cubo.join()

    # Recebe os resultados dos processos
    resultado_quadrado = pipe_quadrado.recv()
    resultado_cubo = pipe_cubo.recv()

    # Exibe os resultados
    print(f"O quadrado de {valor} é: {resultado_quadrado}")
    print(f"O cubo de {valor} é: {resultado_cubo}")


'''
Neste exemplo, dois processos são criados, cada um responsável por calcular o quadrado e o cubo de um número, respectivamente. Os resultados são enviados através dos pipes e depois recebidos no processo principal.

'''