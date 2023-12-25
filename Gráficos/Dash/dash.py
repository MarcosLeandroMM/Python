import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Dados
dados = px.data.iris()

# Layout do aplicativo Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=px.scatter(dados, x='sepal_length', y='sepal_width', color='species', size='petal_length', hover_data=['petal_width']))
])

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
