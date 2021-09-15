import dash
from dash import dcc, html


# export FLASK_ENV=development
app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1('Dash start'),
        dcc.Graph(
            id='example',
            figure={
                'data': [
                    {'x':[1,2,3,4], 'y':[5,6,7,8], 'type': 'line', 'name': 'boats'},
                    {'x':[1,2,3,4], 'y':[8,5,4,7], 'type': 'bar', 'name': 'cars'}
                ],
                'layout': {
                    'title': 'Basic Dash'
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port="8888")
