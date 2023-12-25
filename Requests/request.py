import requests

# Requisições GET para Consultar Dados:
url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro na requisição:', response.status_code)



# Envio de Dados com Requisições POST:
import requests

url = 'https://api.example.com/create'
payload = {'key': 'value'}
response = requests.post(url, data=payload)

if response.status_code == 201:
    print('Recurso criado com sucesso!')
else:
    print('Erro na requisição:', response.status_code)


# Atualização de Dados com Requisições PUT ou PATCH:
import requests

url = 'https://api.example.com/update/1'
payload = {'key': 'new_value'}
response = requests.put(url, data=payload)

if response.status_code == 200:
    print('Recurso atualizado com sucesso!')
else:
    print('Erro na requisição:', response.status_code)


# Exclusão de Dados com Requisições DELETE:
import requests

url = 'https://api.example.com/delete/1'
response = requests.delete(url)

if response.status_code == 204:
    print('Recurso excluído com sucesso!')
else:
    print('Erro na requisição:', response.status_code)


