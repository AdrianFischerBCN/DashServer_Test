
import dash

dash.register_page(__name__,
                   path="/Pruebas",
                   name="Pruebas")

from dash import Dash, dcc, html, Input, Output,  callback
import dash_bootstrap_components as dbc
import plotly.express as px

df = px.data.tips()
days = df.day.unique()

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

day_dropdown = dcc.Dropdown(
    id="dropdown",
    options=[{"label": x, "value": x} for x in days],
    value=days[0],
    clearable=False,
    className="mt-3",
)

fake_dropdown = dbc.Select(
    id="fake-bootstrap-dropdown",
    options=[{"label": x, "value": x} for x in df.sex.unique()],
    value="",
    placeholder="Fake disconnected dropdown for tutorial purposes",
    className="bg-success mt-3"
)


card_question = dbc.Card(
    [
        dbc.CardBody([
            html.H4("Question 1", className="card-title"),
            html.P("What was India's life expectancy in 1952?", className="card-text"),
            dbc.ListGroup(
                children = [
                    dbc.ListGroupItem("A. 55 years", className="m-1"),
                    dbc.ListGroupItem("B. 37 years", className="m-1"),
                    dbc.ListGroupItem("C. 49 years", className="m-1"),
                ],
                flush=False,
                className = "m-2"
            )
        ]),
    ],
    color="warning",

)
layout = dbc.Container([
    card_question
])



if __name__ == "__main__":
    app.run_server(debug=True, port=8002)
