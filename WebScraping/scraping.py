"""Passo a passo

Monitoramento de Preços de Concorrentes
1.Escolha do Site
2.Identificação das tags HTML
3.Utilizar uma biblioteca de raspagem, como BeatifulSoup
4.Iteração e Coleta de Dados
5.Armazenamento em Planilha
6.Análise e Visualização
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = ''
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extrair os dados
nome_produto = soup.find('span', class_='tag').text
preco_produto = soup.find('span', class_='tag').text 

# dataframe que armazenará os dados
df = pd.DataFrame({'Nome do Produto': [nome_produto], 'Preço': [preco_produto]})

# salvando em uma planilha excel
df.to_excel('dados_precos.xlsx', index=False)






