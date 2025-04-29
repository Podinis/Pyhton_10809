# Importamos as bibliotecas essenciais:
import webbrowser #inicio
import pandas as pd # Manipulação de dados
import plotly.express as px # Criação de gráficos interativos
import dash # Framework principal para web app
from dash import dcc, html, Input, Output, State # Componentes Dash
import dash_bootstrap_components as dbc # Componentes visuais com Bootstrap

# 1. Carregamento dos dados:
try:
    titanic_df = pd.read_csv(r"C:\Users\HP\Desktop\Formação\Eisnt\UFCD 10809 - Visualização de dados em Python\titanic.csv") # Dados dos passageiros do Titanic
    happiness_df = pd.read_csv(r"C:\Users\HP\Desktop\Formação\Eisnt\UFCD 10809 - Visualização de dados em Python\happiness_2023.csv") # Relatório mundial da felicidade
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
    exit()

titanic_df = titanic_df.dropna(subset=['Sex', 'Pclass', 'Age', 'Fare', 'Embarked'])
    
# 2. Inicializar a aplicação Dash com tema escuro CYBORG:
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
app.title = "Dashboards Analíticos"

# 3. Definir o layout principal da aplicação:
# Utilizamos dois painéis principais: um para navegação e outro para o conteúdo
app.layout = dbc.Container([
    dbc.Row([
    # Navbar lateral para navegação entre dashboards
        dbc.Col([
        html.H2(" Dashboard", className="text-white text-center my-4"),
        
        dbc.Nav([
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Titanic Dataset", href="/titanic", active="exact"),
            dbc.NavLink("Happiness 2023", href="/happiness", active="exact")
        ], vertical=True, pills=True, className="mb-6")
        
        ], width=2, style={"height": "100vh", "backgroundColor": "#1a1a1a"}),
        
        # Conteúdo principal onde os gráficos e tabelas serão renderizados
        dbc.Col([
            dcc.Location(id="url"), # Controla a URL da aplicação
            html.Div(id="page-content", className="p-4") # Onde os gráficos são mostrados
        ], width=10)
    ]),
    # Footer
    html.Footer(
        dbc.Row([
            dbc.Col([
                html.P("Desenvolvido por Pedro Dinis", className="text-center text-light"),
                html.P("© 2025", className="text-center text-light")
            ], width=12)
        ]),
        style={"backgroundColor": "#1a1a1a", "padding": "10px 0"}
    )
], fluid=True)



def render_titanic():
    # Criar vários gráficos com base nas colunas do dataset Titanic
    fig_sex = px.histogram(titanic_df, x='Sex', title='Distribuição de Passageiros por Sexo', color='Sex')
    fig_pclass = px.histogram(titanic_df, x='Pclass', title='Distribuição por Classe', color='Pclass')
    fig_scatter = px.scatter(titanic_df, x='Age', y='Fare', color='Sex', title='Relação entre Idade e Tarifa')
    fig_box = px.box(titanic_df, x='Pclass', y='Fare', color='Sex', title='Tarifa por Classe e Sexo')
    fig_pie = px.pie(titanic_df, names='Embarked', title='Distribuição por Porto de Embarque')
    fig_fam = px.histogram(titanic_df, x='Family_Size', nbins=10, title='Distribuição do Tamanho da Família')
    fig_age_dist = px.histogram(titanic_df, x='Age', nbins=20, title='Distribuição de Idades dos Passageiros', color='Sex')
    
    return html.Div([
        html.H3("Análise do Dataset Titanic", className="text-info"),
        
        # Distribuir os gráficos em linhas com 3 colunas
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_sex), md=4),
            dbc.Col(dcc.Graph(figure=fig_pclass), md=4),
            dbc.Col(dcc.Graph(figure=fig_fam), md=4)
        ]),
        
        html.Hr(className="text-light"),
        
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_scatter), width=4),
            dbc.Col(dcc.Graph(figure=fig_box), width=4),
            dbc.Col(dcc.Graph(figure=fig_age_dist), width=4)
        ]),
        
        html.Hr(className="text-light"),
        
        # Gráfico de pizza
        dcc.Graph(figure=fig_pie),
        # Amostra dos dados convertida para string para evitar erros
        
        html.H5("Amostra de Dados", className="mt-4 text-light"),
        
        dbc.Table.from_dataframe(titanic_df.head(50).astype(str), striped=True, bordered=True, hover=True, color="dark")
    ])


def render_happiness(selected_country):
    # Filtrar os dados com base no país selecionado
    if selected_country:
        filtered_df = happiness_df[happiness_df['Country name'] == selected_country]
    else:
        filtered_df = happiness_df  # Caso nenhum país seja selecionado, use todos os dados


    # Preparar dados e gráficos
    top10 = happiness_df.sort_values(by="Ladder score", ascending=False).head(10)
    fig_top10 = px.bar(top10, x="Ladder score", y="Country name", orientation='h', title="Top 10 Países mais Felizes", color='Country name')
    fig_hist = px.histogram(happiness_df, x="Ladder score", nbins=20, title="Distribuição do Score de Felicidade")
    
    numeric_cols = happiness_df.select_dtypes(include=['float64', 'int64']).drop(columns=["Standard error of ladder score"])
    fig_corr = px.imshow(numeric_cols.corr(), text_auto=True, title="Correlação entre Variáveis")
     # Gráficos filtrados
    fig_life = px.scatter(filtered_df, x='Healthy life expectancy', y='Ladder score', color='Country name', title='Expectativa de Vida vs Felicidade')
    fig_gdp = px.scatter(filtered_df, x='Logged GDP per capita', y='Ladder score', color='Country name', title='GDP per capita vs Felicidade')
    fig_social = px.scatter(filtered_df, x='Social support', y='Ladder score', color='Country name', title='Apoio Social vs Felicidade')
    fig_freedom = px.scatter(filtered_df, x='Freedom to make life choices', y='Ladder score', color='Country name', title='Liberdade de Escolha vs Felicidade')
    
    return html.Div([
        html.H3("Relatório Mundial da Felicidade - 2023", className="text-success"),
        html.Label("Escolhe o país:"),
        
        # Dropdown para selecionar o país
        dcc.Dropdown(id='dropdown_country',
                options=[{'label': ano, 'value': ano} for ano in sorted(happiness_df['Country name'].unique())],
                value='Portugal',
                clearable=False,
                ),
      
        html.Hr(className="text-light"),
        
        # Primeira linha de gráficos
        dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_top10), md=4),
        dbc.Col(dcc.Graph(figure=fig_hist), md=4),
        dbc.Col(dcc.Graph(figure=fig_corr), md=4)
        ]),
       
        html.Hr(className="text-light"),
        
        # Segunda linha de gráficos
        dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_life), width=4),
        dbc.Col(dcc.Graph(figure=fig_gdp), width=4),
        dbc.Col(dcc.Graph(figure=fig_social), width=4)
        ]),
          
        html.Hr(className="text-light"),
        
        # Terceira linha com um gráfico maior
        dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_freedom), md=6)
        ]),
    html.H5("Amostra de Dados", className="mt-4 text-light"),
    dbc.Table.from_dataframe(happiness_df.head(50).astype(str), striped=True, bordered=True, hover=True,
    color="dark")
])
    
# Função callback para alternar entre as páginas com base na URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def update_page(pathname):
    if pathname == "/" or pathname is None:
        return html.H4("Bem-vindo ao Dashboard Analítico!", className="text-warning")
    elif pathname == "/titanic":
        return render_titanic()
    elif pathname == "/happiness":
        # if selected_country is not None:
        #     return render_happiness(selected_country)
        # else:
            return render_happiness(None)
    else:
        return html.H4("Escolha um dos dashboards no menu à esquerda.", className="text-warning")

webbrowser.open("http://127.0.0.1:8030") #antes do main
if __name__ == "__main__":
    app.run(debug=True, port=8030)