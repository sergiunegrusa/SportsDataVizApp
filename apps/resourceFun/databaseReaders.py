import html as html
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pathlib
import pandas as pd
# Connect to main app.py file
from app import app
from app import server


def getTeamPasses(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Pass']
    aux = aux.loc[aux['outcome'] == 'Successful']
    return aux


def getTeamClearance(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Clearance']
    return aux


def getTeamSavedShot(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'SavedShot']
    return aux


def getTeamMissedShots(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'MissedShots']
    return aux


def getTeamGoals(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Goal']
    return aux

def getTeamTacklesSuccessful(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Tackle']
    aux = aux.loc[aux['outcome'] == 'Successful']
    return aux


def getTeamBallRecovery(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'BallRecovery']
    return aux


def getTeamFoul(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Foul']
    return aux


def getTeamAerials(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'Aerial']
    return aux


def getTeamBlockedPass(teamId, aux):
    aux = aux.loc[aux['teamId'] == teamId]
    aux = aux.loc[aux['type'] == 'BlockedPass']
    aux = aux.loc[aux['outcome'] == 'Successful']
    return aux


def getTeamUnsuccessfulPass(teamId, df):
    df = df.loc[df['teamId'] == teamId]
    df = df.loc[df['type'] == 'Pass']
    df = df.loc[df['outcome'] == 'Unsuccessful']
    return df


def getTeamDispossessed(teamId, df):
    df = df.loc[df['teamId'] == teamId]
    df = df.loc[df['type'] == 'Dispossessed']
    return df


def getPlayerLocations(teamId, playerId, df):
    df = df.loc[df['teamId'] == teamId]
    df = df.loc[df['playerId'] == playerId]
    return df
