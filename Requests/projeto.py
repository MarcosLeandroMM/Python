import requests
import pandas as pd

url = 'https://restcountries.com/v3.1/independent?status=true&fields=languages,capital'

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    dados = []

    for pais in json_data:
        codigo_pais = pais.get('cca3')
        if codigo_pais:
            dados.append({
                'CodigoPais': codigo_pais,
                'Languages': pais.get('languages'),
                'Capital': pais.get('capital')
            })

    df = pd.DataFrame(dados)
    df.to_excel('countries.xlsx', index=False)

    print("Dados salvos com sucesso!")

else:
    print("Erro na solicitação:", response.status_code)
