from PIL import Image
from mplsoccer import Pitch, VerticalPitch
import matplotlib.pyplot as plt

import html as html
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
# Connect to main app.py file
from app import app
from app import server
import plotly.express as px


def fig2img(fig):
    fig.savefig('./assets/pitch2.png')
    plt.close(fig)

def regularPitch():
    pitch = Pitch(pitch_type='statsbomb')
    fig, ax = pitch.draw()
    print(fig)
    print(type(fig))
    fig2img(fig)
    return fig

def verticalPitch():
    pitch = VerticalPitch()
    fig,ax = pitch.draw()
    return fig

def gridPitch(rows_number, columns_number):
    pitch = Pitch()
    fig,axs = pitch.grid(nrows=rows_number, ncols=columns_number)
    return fig

def halfPitch():
    pitch = Pitch(half=True)
    fig,ax = pitch.draw()
    return fig

def halfVerticalPitch():
    pitch = VerticalPitch(half=True)
    fig,ax = pitch.draw()
    return fig

def zonedPitch():
    pitch = Pitch(positional=True, shade_middle=True, positional_color='#eadddd', shade_color='#f2f2f2')
    fig,ax = pitch.draw()
    return fig

def pitchAxis():
    pitch = Pitch(axis=True, label=True, tick=True)
    fig,ax = pitch.draw()
    return fig