"""
A manipulação de arquivos e entrada/saída (I/O) avançada é uma parte importante da programação, e em Python, você pode realizar tarefas avançadas, como trabalhar com arquivos binários, serialização, sockets, streams e manipulação de arquivos grandes. Vou explicar esses conceitos e fornecer exemplos para ilustrar cada um deles:

1. Trabalhando com Arquivos Binários:

Em Python, você pode trabalhar com arquivos binários para ler e gravar dados brutos, como imagens, áudio e qualquer tipo de arquivo binário. Use os modos 'rb' para leitura binária e 'wb' para escrita binária.

Exemplo de leitura de um arquivo binário:
"""

with open('arquivo_binario.png', 'rb') as arquivo:
    dados = arquivo.read()
    # Processar dados binários

"""
 Serialização Avançada:

Python oferece bibliotecas avançadas para serializar dados em vários formatos, como JSON, XML, Pickle e MessagePack. Essas bibliotecas permitem que você armazene, transmita e recupere dados de forma estruturada.

Exemplo de serialização e desserialização usando JSON:
"""

import json

dados = {"nome": "Alice", "idade": 30}
# Serializar dados para JSON
dados_json = json.dumps(dados)

# Desserializar dados do JSON
dados_recuperados = json.loads(dados_json)

"""
 Sockets e Comunicação em Rede:

Python oferece suporte para comunicação em rede por meio da biblioteca socket. Você pode criar servidores e clientes para trocar dados pela rede.

Exemplo de um servidor simples:

"""

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))
servidor.listen(5)

while True:
    cliente, endereco = servidor.accept()
    mensagem = cliente.recv(1024)
    # Processar mensagem
    cliente.close()


"""
Streams:

Streams são fluxos contínuos de dados que podem ser lidos ou gravados em partes menores. Em Python, você pode usar io para criar streams personalizados.

Exemplo de leitura de um stream:

"""

from io import BytesIO

stream = BytesIO(b'Dados de exemplo')
parte = stream.read(5)
# Processar parte dos dados

"""
Manipulação de Arquivos Grandes:

Para manipular arquivos grandes sem carregá-los na memória inteiramente, você pode ler e processar arquivos em partes.

Exemplo de leitura de arquivo grande em partes
"""

tamanho_do_bloco = 4096  # Tamanho do bloco em bytes

with open('arquivo_grande.txt', 'rb') as arquivo:
    while True:
        parte = arquivo.read(tamanho_do_bloco)
        if not parte:
            break
        # Processar a parte lida



