import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import plotly.express as px
import pandas as pd


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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
                dbc.NavLink("Encomendas", href="/page-1", active="exact"),
                dbc.NavLink("Vendas", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

# Carregar dataset   
df = px.data.gapminder()

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"),
               [Input("url", "pathname")])


def render_page_content(pathname):
    if pathname == "/":
        return html.H1("🌍🌍 Dashboard Home", style={"textAlign": "center"})
    

    elif pathname == "/page-1":
    
        fig1 = px.scatter(
        df,
        x="gdpPercap", y="lifeExp",
        size="pop", color="continent",
        hover_name="country", log_x=True,
        title=f"Esperança de vida vs PIB per capita "
        )

        return html.Div([
            html.H1("🌍🌍 Encomendas", style={"textAlign": "center"}),
            #Dropdown para escolher ano
            html.Label("Escolhe o ano:", style={"fontSize": 20, "textAlign": "center", "fontWeight": "bold"}),
            dcc.Dropdown(
                id='dropdown-ano',
                options=[{'label': ano, 'value': ano} for ano in sorted(df['year'].unique())],
                value=2007,
                clearable=False,
                style={'width': '140px'}
            ),

            dcc.Graph(fig1)

        ])
    
    elif pathname == "/page-2":
        return  html.H1("🌍🌍 Vendas", style={"textAlign": "center"})
    # If the user tries to reach a different page, return a 404 message
    
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run(port=8888)