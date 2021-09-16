import os
import json

import dash

from tqdm import tqdm
from dash import dcc, html
import plotly.express as px

import numpy as np
import pandas as pd

with open("tiles_dates.json") as f:
    tile_dates_dict = json.loads(f.read())

date_tile_kv = {}
unique_dates = set()

for til in tile_dates_dict.keys():
    for da in tile_dates_dict[til]:
        unique_dates.add(da)
unique_dates = list(unique_dates)

for date_ in unique_dates:
    # date_tile_kv[date_] = []
    for til in tile_dates_dict.keys():
        if date_ in tile_dates_dict[til]:
            date_tile_kv[date_] = int(til)
            # date_tile_kv[date_].append(int(til))


df = pd.DataFrame(
    {"date": list(date_tile_kv.keys()), "tiles": list(date_tile_kv.values())}
)

# df = df.astype({"date": str, "tiles": int})
# df = df.transpose()
df = df.sort_values('date')
# df['date'] = pd.to_datetime(df['date'])

fig = px.scatter(
    df, x="date", y="tiles"
    # df, x=list(date_tile_kv.keys()), y=list(date_tile_kv.values()),
)
# fig.update_xaxes(type='category')


# export FLASK_ENV=development
app = dash.Dash(
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)


app.layout = html.Div(
    html.Div([
        html.H3(f'date distribution of tiles'),
        dcc.Graph(
            id=f'date_tile',
            figure=fig
        )]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8888)
