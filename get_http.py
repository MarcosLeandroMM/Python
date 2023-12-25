import http.client

def http_get(url):
    try:
        # Analisa a URL para obter o host, o caminho e a porta (se fornecida)
        url_parts = http.client.urlsplit(url)
        host = url_parts.netloc
        path = url_parts.path
        if not path:
            path = '/'  # Use "/" como caminho padrão se não especificado

        # Cria uma conexão HTTP com o servidor
        conn = http.client.HTTPSConnection(host)

        # Envia uma solicitação GET
        conn.request("GET", path)

        # Obtém a resposta do servidor
        response = conn.getresponse()

        # Lê e exibe a resposta
        data = response.read()
        print(f'Resposta do servidor:\n{data.decode()}')

        # Fecha a conexão
        conn.close()

    except Exception as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")

if __name__ == '__main__':
    url = input("Digite a URL para a solicitação GET: ")
    http_get(url)