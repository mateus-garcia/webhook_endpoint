import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components import Div

from .app import app
from .side_bar import sideBar

layout: Div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='subsub1_sidebar'),
    html.H1('This is a dummy sub sub sub app')
])


@app.callback(
    Output('subsub1_sidebar', 'children'),
    [Input('url', 'pathname')]
)
def menu(pathname):
    return sideBar(pathname)
