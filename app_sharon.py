import os
import json
from datetime import datetime
from itertools import groupby

import dash

from tqdm import tqdm
from dash import dcc, html
import plotly.express as px

import numpy as np
import pandas as pd

df = pd.read_csv("20211112_ICLRKenya_training_final.csv")

print(f"Len of df is: {len(df)}")

"""
dates_ = df.columns.tolist()[5:]
dates_ = [list(g) for k,g in groupby(dates_, key=lambda x: x.split("_")[0])]
dates_ = [x[0].split("_")[0] for x in dates_]
dates_ = [datetime(int(x[:4]),int(x[4:6]),int(x[6:])) for x in dates_]
"""
fig = px.scatter(
    y=df.iloc[0][5:], x=df.columns.tolist()[5:]
)

# export FLASK_ENV=development
app = dash.Dash(
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)


app.layout = html.Div(
    html.Div([
        html.H3(f'date distribution of labels'),
        dcc.Graph(
            id=f'date_tile',
            figure=fig
        )]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8888)
