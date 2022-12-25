import dash

dash.register_page(__name__,
                   path="/",
                   name="Huuuula")

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

card = dbc.Card(
    [
        html.Div(
            children=dbc.CardImg(
                src="/assets/hug.jpg",
                top=True),
            hidden = True,
            id="DivConImg"
        ),
        dbc.CardBody(
            children=[
                html.H4("Achuuuche!", className="card-title"),
                html.P("Mua mua mua mua"),
                html.P("Haz clic para añadir más achuches"),
                html.P("Total de achuches = 0")],
            id="CardBody"),
        dbc.Button(
            children="Achuche!",
            n_clicks=0,
            color="primary",
            id="BtnIncrementar")
    ],
    style={"width": "18rem"},
)

layout = html.Div(
    [
        html.H1("Buenos días!"),
        dbc.Row([
            dbc.Col(
                children = "",
                width = 1),
            dbc.Col(
                children=card)
        ])
    ])


@callback(
    Output('CardBody', 'children'),
    Output("DivConImg","hidden"),
    Input('BtnIncrementar', 'n_clicks'),
)
def update_output(n_clicks):
    list_resultado=[
        html.H4("Achuuuche!", className="card-title"),
        html.P("Mua mua mua mua"),
        html.P("Haz clic para añadir más achuches"),
        html.P("Total de achuches = " + str(n_clicks))]

    if n_clicks > 0:
        EsconderImagen = False
    else:
        EsconderImagen = True
    return list_resultado,EsconderImagen

