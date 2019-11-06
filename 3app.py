import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html


# export FLASK_ENV=development
app = dash.Dash()


start = datetime.datetime(2019, 1, 6)
end = datetime.datetime(2019, 11, 6)

df = web.DataReader('^DJI', 'stooq')

# print(df.head())

# df.reset_index(inplace=True)
# df.set_index('Date', inplace=True)
# df = df.drop('Symbol', axis=1)
# import pdb; pdb.set_trace()
# print(df.head())
# print(df.info())

app.layout = html.Div(
    children=[
        html.H1('wtf is DJI'),
        dcc.Graph(
            id='example',
            figure={
                'data': [
                    {'x': df.index, 'y':df.Close, 'type': 'line', 'name': 'DJI'},
                ],
                'layout': {
                    'title': 'DJI'
                }
            }
        )
    ]
)

if __name__ == '__main__':


    app.run_server(debug=True, host='0.0.0.0')
