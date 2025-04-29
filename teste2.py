import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# Carregar dataset
df = px.data.gapminder()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Grafico", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# Callback para atualizar gráficos com base no dropdown
@app.callback(
    [
        Output("page-content", "children"),
        Output("grafico-dispersao", "figure"),
        Output("histograma-populacao", "figure"),
        Output("barra-populacao", "figure"),
    ],
    [
        Input("url", "pathname"),
        Input("dropdown-ano", "value"),
    ],
)
            
            
def atualizar_conteudo_e_graficos(pathname, ano_selecionado):
    if ano_selecionado is None:
       ano_selecionado = 2007  # ou qualquer ano padrão que você queira


    if pathname == "/":
        pag0 = html.Div(
            [
                html.H1("Home", className="display-4"),
                html.P("Welcome to the home page!", className="lead"),
            ]
        )
        return pag0, {}, {}, {}

    elif pathname == "/page-1":
        # Filtrar os dados com base no ano selecionado
        dados_filtrados = df[df['year'] == ano_selecionado]

        # Criar os gráficos
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

        fig3 = px.treemap(
            dados_filtrados,
            path=['continent', 'country'],
            values='pop',
            color='lifeExp',
            title=f"Distribuição Populacional por Continente ({ano_selecionado})"
        )

        # Conteúdo da página 1
        pag1 = html.Div(
            [
                html.H1("🌍🌍 Dashboard Interativo - Gapminder", style={"textAlign": "center"}),
                html.Label("Escolhe o ano:", style={"fontSize": 20, "textAlign": "center", "fontWeight": "bold"}),
                dcc.Dropdown(
                    id='dropdown-ano',
                    options=[{'label': ano, 'value': ano} for ano in sorted(df['year'].unique())],
                    value=ano_selecionado,
                    clearable=False,
                    style={'width': '140px'}
                ),
                # Gráfico de dispersão
                dcc.Graph(id='grafico-dispersao'),

                html.Div(
                    [
                        # Histograma de população
                        dcc.Graph(id='histograma-populacao', style={'flex': '1'}),

                        # Barra de população
                        dcc.Graph(id='barra-populacao', style={'flex': '1'}),
                    ],
                    style={'display': 'flex', 'justifyContent': 'space-between'}
                )
            ]
        )
        return pag1, fig1, fig2, fig3

    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!"), {}, {}, {}

    # Se o usuário tentar acessar uma página inexistente
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    ), {}, {}, {}


if __name__ == "__main__":
    app.run(port=8888)