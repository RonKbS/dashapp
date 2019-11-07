import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# export FLASK_ENV=development
app = dash.Dash()

# https://stooq.com/t/
stook_indices = [
    {'label': 'HANG SENG', 'value': '^TWSE'},
    {'label': 'DOW JONES INDU', 'value': '^DJI'},
    {'label': 'NIKKEI225', 'value': '^NKX'},
    {'label': 'JCI', 'value': '^JCI'},
    {'label': 'ALL ORDINARIES', 'value': '^AOR'}
]

app.layout = html.Div(
    children=[
        html.Div(
            children='''symbol to graph'''
        ),
        dcc.Dropdown(
            id='dropdown',
            value='^AOR',
            options=stook_indices
        ),
        html.Div(id='output-graph')
    ]
)


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_value(value):
    df = web.DataReader(value, 'stooq')
    
    return dcc.Graph(
        id='stooq',
        figure={
            'data': [
                {'x': df.index, 'y':df.Close, 'type': 'line', 'name': value},
            ],
            'layout': {
                'title': value
            }
        }
    )



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
