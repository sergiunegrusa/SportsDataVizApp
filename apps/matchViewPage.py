import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime
import pathlib
import numpy as np
from app import app
from apps.resourceFun.interpretData import teamPasses, getPitchPlotly
from apps.resourceFun.plotFunctions import plotLostBalls, plotTackle, plotPasses, plotSavedShots, plotGoals, plotFouls, \
    plotAerials

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv('./datasets/europaFinal.csv')
print(df[:15])


#Layout section: Bootstrap
# --------------------------
layout = dbc.Container([

    html.H1('Sports Data Viz Tool', style={'textAlign': 'center'}),
    html.Div([
        dcc.Dropdown(id='selected_team', multi=False, value='Manchester United',
                     options=[{'label': x, 'value': x}
                              for x in sorted(df['teamId'].unique())],
                     className='row, mb-4', style={'width': '50%'}),
        dcc.Dropdown(id='selected_period', multi=False, value='FirstHalf',
                             options=['FirstHalf', 'SecondHalf', 'FirstPeriodOfExtraTime', 'SecondPeriodOfExtraTime',
                                      'Match'],
                             className='row, mb-4', style={'width': '50%'}),
        dcc.Checklist(id='selected_plots',
                      options=[{'label': x, 'value': x}
                               for x in sorted(['Tackles', 'Aerials', 'Fouls', 'Goals',
                               'Lost Balls', 'Saved Shots', 'Passes'])],
                      className='row, mb-4', style={'width': '50%'},
                      labelStyle={'display': 'inline', 'cursor': 'pointer', 'margin-left': '20px'}),
    ]),

    html.Div([
        dcc.Graph(id='graph1', figure={}, style={'width': '90vh', 'height': '60vh'}),
    ]),

    dcc.Store('store_data', data=[], storage_type='memory'),
])


#plot data on dash
@app.callback(
    Output('graph1', 'figure'),
    [Input('selected_team', 'value'), Input('selected_period', 'value'),
     Input('selected_plots', 'value')],
    prevent_initial_call=False
)

def changeTeamPlot(chosen_team, chosen_period, chosen_plot):
    aux = df
    print(f'val chosen: {chosen_team}')
    print(type(chosen_team))

    pitch = getPitchPlotly("./assets/pitch.png")

    if chosen_period != 'Match':
        aux = aux.loc[aux['period'] == chosen_period]

    print(chosen_plot)
    print(type(chosen_plot))

    if chosen_plot != None:
        if 'Passes' in chosen_plot:
            pitch = plotPasses(chosen_team, aux, pitch)
        if 'Tackles' in chosen_plot:
            pitch = plotTackle(chosen_team, aux, pitch)
        if 'Saved Shots' in chosen_plot:
            pitch = plotSavedShots(chosen_team, aux, pitch)
        if 'Goals' in chosen_plot:
            pitch = plotGoals(chosen_team, aux, pitch)
        if 'Fouls' in chosen_plot:
            pitch = plotFouls(chosen_team, aux, pitch)
        if 'Aerials' in chosen_plot:
            pitch = plotAerials(chosen_team, aux, pitch)
        if 'Lost Balls' in chosen_plot:
            pitch = plotLostBalls(chosen_team, aux, pitch)


    # print(fig)
    # print(type(fig))
    return pitch
