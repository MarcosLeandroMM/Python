'''

O paralelismo em tarefas de entrada/saída (E/S) pode ser benéfico para melhorar o desempenho quando há operações bloqueantes, como leitura ou gravação de arquivos, que não dependem principalmente da CPU. Usar processos pode ser uma abordagem eficaz para aproveitar esse tipo de paralelismo. Aqui está um exemplo simples usando a biblioteca concurrent.futures para executar operações de leitura e gravação em arquivos em paralelo:

'''

import concurrent.futures

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

def escrever_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

if __name__ == "__main__":
    # Lista de arquivos para leitura e gravação
    arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]

    # Usar ProcessPoolExecutor para executar operações de E/S em paralelo
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Operações de leitura em paralelo
        resultados_leitura = list(executor.map(ler_arquivo, arquivos))

        # Operações de gravação em paralelo
        dados_para_escrever = ["Texto para o arquivo 1", "Texto para o arquivo 2", "Texto para o arquivo 3"]
        list(executor.map(escrever_arquivo, arquivos, dados_para_escrever))

    # Exibir os resultados da leitura
    print("Resultados da leitura:")
    for nome_arquivo, resultado in zip(arquivos, resultados_leitura):
        print(f"{nome_arquivo}: {resultado}")

    # Exibir os resultados da gravação
    print("\nResultados da gravação:")
    for nome_arquivo in arquivos:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"{nome_arquivo}: {conteudo}")
