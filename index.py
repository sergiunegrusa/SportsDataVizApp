import html as html

import matplotlib.pyplot as plt
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
# from mplsoccer import Pitch, VerticalPitch
import plotly.express as px
import plotly.graph_objs as go
import plotly.tools as tls
import tkinter as tk
import numpy as np

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import matchViewPage

# from apps.resourceFun.pitchTypes import *
from apps.resourceFun.databaseReaders import *
from apps.resourceFun.interpretData import *
from apps.resourceFun.plotFunctions import plotTackle, plotPasses, plotSavedShots, plotGoals, plotFouls, plotAerials, \
    plotLostBalls
from apps.resourceFun.uploadFromFolder import save_file, file_download_link, uploaded_files

PATH = pathlib.Path()
DATA_PATH = PATH.joinpath("../datasets").resolve()

# df = pd.read_csv('./datasets/europaFinal.csv')

# Layout section: Bootstrap
# --------------------------
app.layout = dbc.Container([
    html.Div(
        [
            html.H1("File Browser"),
            html.H2("Upload"),
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    ["Drag and drop or click to select a file to upload."]
                ),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=True,
            ),
            html.H2("File List"),
            dcc.Link(
                html.Ul(id="file-list"), href='/apps/matchViewPage'
            ),
        ],
        style={"max-width": "500px"},
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


#upload file
@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)
        df = pd.read_csv(uploaded_filenames)
    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]


#move to different page
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")],
)
def display_page(pathname):
    if pathname == '/apps/matchViewPage':
        return matchViewPage.layout
    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=False)
