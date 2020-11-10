import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .app import app
from .side_bar import sideBar

a = -200

layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='app1_sidebar'),
    html.H3('App 1'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-1-display-value'),
    dcc.Interval(id='interval-component', interval=1. * 1000, n_intervals=10),
    html.Div(id='output-block'),
    html.Div(html.P(a)),
    dcc.Link('Go to App 2', href='/apps/app2')
])


@app.callback(
    Output('output-block', 'children'),
    [Input('interval-component', 'n_intervals')])
def update(interval_value):
    global a
    a += 1
    # print('Internal interval value: {}'.format(interval_value))
    return 'The interval value is: {}'.format(a)


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('app1_sidebar', 'children'),
    [Input('url', 'pathname')]
)
def menu(pathname):
    return sideBar(pathname)
