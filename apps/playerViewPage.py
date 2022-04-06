import dash_bootstrap_components as dbc
from dash import dcc, html
import pathlib
import pandas as pd
from dash.dependencies import Output, Input
from app import app
from apps.resourceFun.intra_match_performance import playerInterestZone

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv('./datasets/europaFinal.csv')


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

        dcc.Dropdown(id='selected_player', multi=False, value='1',
                             options=[],
                             className='row, mb-4', style={'width': '50%'}),

        dcc.Checklist(id='selected_plots',
                      options=[{'label': x, 'value': x}
                               for x in sorted(['Tackles', 'Aerials', 'Fouls', 'Goals', 'Lost Balls', 'Saved Shots',
                                                'Passes'])],
                      className='row, mb-4', style={'width': '50%'},
                      labelStyle={'display': 'inline', 'cursor': 'pointer', 'margin-left': '20px'}),
    ]),

    html.Div([
        dcc.Graph(id='graph1', figure={}, style={'width': '90vh', 'height': '60vh'}),
    ]),
])

#plot data on dash
@app.callback(
    Output('selected_player', 'options'),
    [Input('selected_team', 'value')],
    prevent_initial_call=False
)
def populatePlayerList(selected_team):
    aux = df
    aux = aux.loc[aux['teamId'] == selected_team]
    aux = aux['playerId'].unique()
    aux = aux.tolist()
    cleanedList = [x for x in aux if str(x) != 'nan']
    print(aux)
    return cleanedList


@app.callback(
    Output('graph1', 'figure'),
    [Input('selected_team', 'value'), Input('selected_period', 'value'), Input('selected_player', 'value'),
     Input('selected_plot', 'value')]
)
def plotFunctions(selected_team, selected_period, selected_player, selected_plot):
    aux = df
    pitch = playerInterestZone(selected_team, selected_player, selected_period, aux)
    print(pitch)
    return pitch



