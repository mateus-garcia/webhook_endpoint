import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .app import app
from .side_bar import sideBar

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='app2_sidebar'),
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])


@app.callback(
    Output('app2_sidebar', 'children'),
    [Input('url', 'pathname')]
)
def menu(pathname):
    return sideBar(pathname)