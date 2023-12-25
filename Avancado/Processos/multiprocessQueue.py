import multiprocessing

def calcular_quadrado(numero, fila):
    resultado = numero * numero
    fila.put(resultado)

def calcular_cubo(numero, fila):
    resultado = numero * numero * numero
    fila.put(resultado)

if __name__ == "__main__":
    # Criação de fila para comunicação entre processos
    fila_resultados = multiprocessing.Queue()

    # Valores para cálculo
    valor = 5

    # Criando processos para calcular quadrado e cubo em paralelo
    processo_quadrado = multiprocessing.Process(target=calcular_quadrado, args=(valor, fila_resultados))
    processo_cubo = multiprocessing.Process(target=calcular_cubo, args=(valor, fila_resultados))

    # Inicia os processos
    processo_quadrado.start()
    processo_cubo.start()

    # Aguarda a conclusão dos processos
    processo_quadrado.join()
    processo_cubo.join()

    # Recebe os resultados da fila
    resultado_quadrado = fila_resultados.get()
    resultado_cubo = fila_resultados.get()

    # Exibe os resultados
    print(f"O quadrado de {valor} é: {resultado_quadrado}")
    print(f"O cubo de {valor} é: {resultado_cubo}")

'''
Neste exemplo, a fila fila_resultados é compartilhada entre os dois processos. Cada processo coloca o resultado na fila usando o método put, e o processo principal retira os resultados usando o método get. A fila é uma maneira eficaz de passar dados entre processos de maneira segura.

'''