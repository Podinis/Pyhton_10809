# Carregar bibliotecas
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd


# Carregar dataset
df = px.data.gapminder()

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("🌍🌍 Dashboard Interativo - Gapminder", style={"textAlign": "center"}),

    # Dropdown para escolher o ano
    html.Label("Escolhe o ano:", style={"fontSize": 20, "textAlign": "center","fontWeight": "bold"}),
    dcc.Dropdown(id='dropdown-ano',
                options=[{'label': ano, 'value': ano} for ano in sorted(df['year'].unique())],
                value=2007,
                clearable=False,
                style={'width': '140px'}
                ),

    # Gráfico de dispersão
    dcc.Graph(id='grafico-dispersao'),  
  
    html.Div([
               
        # Histograma de população
        dcc.Graph(id='histograma-populacao', style={'flex': '1'}),
        
        # Barra de população
        dcc.Graph(id='barra-populacao', style={'flex': '1'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'})
    
])



# Callback para atualizar gráficos com base no dropdown
@app.callback(
            [Output('grafico-dispersao', 'figure'),
            Output('histograma-populacao', 'figure'),
            Output('barra-populacao', 'figure')
            ],
            [Input('dropdown-ano', 'value')]
            )


def atualizar_graficos(ano_selecionado):
    dados_filtrados = df[df['year'] == ano_selecionado]
    
    fig1 = px.scatter(
        dados_filtrados,
        x="gdpPercap", y="lifeExp",
        size="pop", color="continent",
        hover_name="country", log_x=True,
        title=f"Esperança de vida vs PIB per capita ({ano_selecionado})"
    )
    
    fig2 = px.histogram(
        dados_filtrados,
        x="pop", nbins=20, color="continent",
        title=f"Distribuição Populacional por País ({ano_selecionado})"
    )
    
    
    fig3 = px.treemap(dados_filtrados,
        path=['continent', 'country'],
        values='pop',
        color='lifeExp',
        title=f"Distribuição Populacional por Continente ({ano_selecionado})"
        )


    
    return fig1, fig2 , fig3

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)