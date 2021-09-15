import os
import json

import dash

from tqdm import tqdm
from dash import dcc, html
import plotly.express as px

import numpy as np
import pandas as pd

df_kidoz = []
for band in [2,3,4,8]:
    df = pd.read_csv(
        f"averaged_b0{band}_train_data.csv",
        dtype={
            "0": np.float32, "1": np.float32, "2": np.float32,
            "3": np.float32, "4": np.float32, "5": np.float32,
            "6": np.float32, "7": np.float32, "8": np.float32,
            "9": np.float32, "label": int, "field_id": int
        }
    )
    with open("field_tile_id.json") as f:
        maa = json.loads(f.read())
    l_maa = [[int(key), int(val)] for key, val in maa.items()]
    df_maa = pd.DataFrame(data=l_maa, columns={"field_id", "tile_id"})
    for index, row in tqdm(df.iterrows()):
        # import pdb;pdb.set_trace()
        df.loc[
            df["field_id"]==int(row["field_id"]), "tile_id"
        ] = maa[str(int(row["field_id"]))]
    # df = df.merge(df_maa, on="field_id")
    # df.drop("field_id", inplace=True, axis=1)
    import pdb;pdb.set_trace()

    # fig = px.scatter_3d(
    #     df, x=df["0"], y=df["tile_id"],
    #     z=df["label"], color="label"
    # )
    fig = px.scatter(
        df, x=df["0"], y=df["tile_id"] 
    )
    df_kidoz.append(
        html.Div([
            html.H3(f'band 0{band} first date values'),
            dcc.Graph(
                id=f'band_0{band}',
                figure=fig
            )], className="six columns"
        )
    )

# export FLASK_ENV=development
app = dash.Dash(
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)


app.layout = html.Div([
    html.Div([df_kidoz[0], df_kidoz[1]], className="row"),
    html.Div([df_kidoz[2], df_kidoz[3]], className="row")
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8888)
