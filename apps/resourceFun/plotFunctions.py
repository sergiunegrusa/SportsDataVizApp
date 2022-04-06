from apps.resourceFun.interpretData import *
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
import plotly.tools as tls


def plotPasses(teamId, aux, fig):
    passes = teamPasses(teamId, aux)
    x = passes.x * 1.2
    x = x.tolist()
    y = passes.y * 0.8
    y = y.tolist()
    for value in y:
        if value > 80:
            print('found one')
            print(value)
    endX = passes.endX * 1.2
    endX = endX.tolist()
    endY = passes.endY * 0.8
    endY = endY.tolist()
    print()
    for value in range(len(x)):
        aux1 = []
        aux2 = []

        aux1.append(x[value])
        aux1.append(endX[value])

        aux2.append(y[value])
        aux2.append(endY[value])

        fig.add_trace(go.Scatter(x=aux1, y=aux2,
                                 mode='lines',
                                 name='Passes',
                                 line=dict(color='#ADD8E6')))
    fig.update(layout_showlegend=False)
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False, xaxis_rangeslider_visible=False)
    return fig



def plotTackle(teamId, aux, fig):
    tackles = getRecovery(teamId, aux)
    tackles.x = tackles.x * 1.2
    tackles.y = tackles.y * 0.8
    player_id = tackles.playerId
    fig.add_trace(go.Scatter(x=tackles.x, y=tackles.y,
                             mode='markers',
                             name='Tackles',
                             hovertext=tackles.playerId))
    fig.update_traces(marker_size=10)
    # print(fig)
    print(type(fig))
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False)
    return fig


def plotSavedShots(teamId, aux, fig):
    result = teamSavedShot(teamId, aux)
    x = result.x * 1.2
    y = result.y * 0.8
    endX = 120 * 1.2
    endY = 40 * 0.8
    x = x.tolist()
    y = y.tolist()

    for value in range(len(x)):
        aux1 = []
        aux2 = []

        aux1.append(x[value])
        aux1.append(endX)
        print('aux1: ')
        print(aux1)

        aux2.append(y[value])
        aux2.append(endY)
        print('aux2: ')
        print(aux2)

        fig.add_trace(go.Scatter(x=aux1, y=aux2,
                                 mode='lines',
                                 name='Saved Shots',
                                 line=dict(color='#ADD8E6')))
    print(type(fig))
    fig.update(layout_showlegend=False)
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False, xaxis_rangeslider_visible=False)
    return fig


def plotGoals(teamId, aux, fig):
    goals = getTeamGoals(teamId, aux)
    x = goals.x * 1.2
    y = goals.y * 0.8
    endX = 120
    endY = 40
    x = x.tolist()
    y = y.tolist()

    for value in range(len(x)):
        aux1 = []
        aux2 = []

        aux1.append(x[value])
        aux1.append(endX)

        aux2.append(y[value])
        aux2.append(endY)

        fig.add_trace(go.Scatter(x=aux1, y=aux2,
                                 mode='lines',
                                 name='Goals',
                                 line=dict(color='#ADD8E6')))
    fig.update(layout_showlegend=False)
    fig.update_xaxes(range=(-8, 128))
    fig.update_yaxes(range=(-10, 90))
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False, xaxis_rangeslider_visible=False)
    return fig


def plotFouls(teamId, aux, fig):
    foul = getTeamFoul(teamId, aux)
    foul.x = foul.x * 1.2
    foul.y = foul.y * 0.8
    player_id = foul.playerId

    fig.add_trace(go.Scatter(x=foul.x, y=foul.y,
                             mode='markers',
                             name='Fouls',
                             hovertext=foul.playerId))
    fig.update_traces(marker_size=10)
    # print(fig)
    print(type(fig))
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False)
    return fig


def plotAerials(teamId, aux, fig):
    aerial = getTeamAerials(teamId, aux)
    aerial.x = aerial.x * 1.2
    aerial.y = aerial.y * 0.8
    player_id = aerial.playerId

    fig.add_trace(go.Scatter(x=aerial.x, y=aerial.y,
                             mode='markers',
                             name='Aerials',
                             hovertext=aerial.playerId))
    fig.update_traces(marker_size=10)
    # print(fig)
    print(type(fig))
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False)
    return fig


def plotLostBalls(teamId, aux, fig):
    lost_ball = getLostBallActions(teamId, aux)
    lost_ball.x = lost_ball.x * 1.2
    lost_ball.y = lost_ball.y * 0.8
    player_id = lost_ball.playerId

    fig.add_trace(go.Scatter(x=lost_ball.x, y=lost_ball.y,
                             mode='markers',
                             name='Lost Balls',
                             hovertext=lost_ball.playerId))
    fig.update_traces(marker_size=10)
    # print(fig)
    print(type(fig))
    # fig.update_layout(template="plotly_white", xaxis_showgrid=False, yaxis_showgrid=False)
    return fig