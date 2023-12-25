import plotly.express as px

# Dados
dados = px.data.iris()

# Gráfico de dispersão interativo
fig = px.scatter(dados, x='sepal_length', y='sepal_width', color='species', size='petal_length', hover_data=['petal_width'])

# Exibindo o gráfico
fig.show()
