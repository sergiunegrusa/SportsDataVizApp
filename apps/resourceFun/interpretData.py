import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns
from scipy.spatial.qhull import ConvexHull
from pywaffle import Waffle

import plotly.graph_objects as go
import plotly.express as px

import html as html
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pathlib
# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import matchViewPage

from apps.resourceFun.pitchTypes import *
from apps.resourceFun.databaseReaders import *

def getPitchPlotly(source):
    from PIL import Image
    fig = go.Figure()
    pitch = Image.open(source)
    fig.add_layout_image(
        dict(
            source=pitch,
            xref="paper",
            yref="paper",
            x=0,
            y=1,
            xanchor="left",
            yanchor="top",
            sizex=1.0,
            sizey=1.0,
            sizing="stretch",
            opacity=0.5,
            layer="below"
            )
    )
    fig.update_xaxes(showgrid=False, range=(-8, 128))
    fig.update_yaxes(showgrid=False, range=(-10, 90))

    return fig


def teamPasses(teamId, df):
    teamPasses = getTeamPasses(teamId, df)
    teamClearance = getTeamClearance(teamId, df)
    frames = [teamPasses, teamClearance]
    result = pd.concat(frames)
    return result


def teamSavedShot(teamId, aux):
    df = getTeamSavedShot(teamId, aux)
    df2 = getTeamMissedShots(teamId, aux)
    frames = [df, df2]
    result = pd.concat(frames)
    print(result)
    return result


def getRecovery(teamId, aux):
    df = getTeamTacklesSuccessful(teamId, aux)
    print(len(df))
    df2 = getTeamBallRecovery(teamId, aux)
    frames = [df, df2]
    result = pd.concat(frames)
    print(result)
    return result


def getLostBallActions(teamId, aux):
    df = getTeamBlockedPass(teamId, aux)
    df2 = getTeamUnsuccessfulPass(teamId, aux)
    df3 = getTeamDispossessed(teamId, aux)

    frames = [df, df2, df3]
    result = pd.concat(frames)
    return result


