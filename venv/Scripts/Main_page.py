import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .app import app
from .side_bar import sideBar

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H3('Main page'),
    html.Div(id='sideBar'),

    html.Div(children=[

        html.H2(dcc.Link('App1', href='/app1')),
        html.Br(),
        html.H4(dcc.Link('App2', href='/app2')),
        html.Br(),

    ], style={'width': '20%', 'display': 'inline_block', 'background-color': '#c1c3c7'}),
])


@app.callback(
    Output('sideBar', 'children'),
    [Input('url', 'pathname')]
)
def menu(pathname):
    return sideBar(pathname)
