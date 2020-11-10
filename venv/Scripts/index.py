import Main_page
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from .app import app
from .apps import app1, app2
from .apps.app1 import sub1, sub2
from .apps.app1.sub_1 import subsub1, subsub2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    elif pathname == '/apps/app1/sub_1':
        return sub1.layout
    elif pathname == '/apps/app1/sub_1/subsub1':
        return subsub1.layout
    elif pathname == '/apps/app1/sub_1/subsub2':
        return subsub2.layout
    elif pathname == '/apps/app1/sub_2':
        return sub2.layout
    else:
        return Main_page.layout


if __name__ == '__main__':
    app.run_server(debug=True)
