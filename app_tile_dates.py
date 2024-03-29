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
tile_date_kv = []
unique_dates = set()

for til in tile_dates_dict.keys():
    for da in tile_dates_dict[til]:
        unique_dates.add(da)
unique_dates = list(unique_dates)


for til in tile_dates_dict.keys():
    for da_ in tile_dates_dict[til]:
        tile_date_kv.append([til, da_])

tile_date_kv = np.array(tile_date_kv)

df = pd.DataFrame(tile_date_kv, columns=["tiles", "date"])
# import pdb;pdb.set_trace()
# df = df.astype({"date": str, "tiles": int})
# df = df.transpose()
df = df.sort_values('tiles')
# df['date'] = pd.to_datetime(df['date'])

fig = px.scatter(
    df, x="date", y="tiles", color="tiles"
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
