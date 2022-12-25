'''
 # @ Create Time: 2022-12-25 11:01:56.161373
'''

import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__,
                use_pages=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                assets_folder="assets",
                title="MultiPageApp")

server = app.server

sidebar = dbc.Nav(
            children=[
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Row([
    dbc.Col(
        children=sidebar,
        width=2
    ),
    dbc.Col(
        children=dash.page_container,
        width=9
    )]

)



if __name__ == "__main__":
    app.run_server(debug=True)
