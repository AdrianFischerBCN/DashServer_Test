import dash

dash.register_page(__name__,
                   name="Melodía despertador")

from dash import Dash, dcc, html
import numpy as np

np.random.seed(2020)

layout = html.Div([
    html.H1("Melodía despertador"),
    html.P(
        children="Clic para reproducir"
    ),
    html.Audio(id='audio',
               controls=True,
               src="/assets/makina.mp3")
    ]
)



