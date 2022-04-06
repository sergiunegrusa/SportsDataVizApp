import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns
from scipy.spatial.qhull import ConvexHull
from pywaffle import Waffle
from PIL import Image
import plotly.graph_objects as go


def playerInterestZone(teamId, playerId, period, df):
    df = df.loc[df['teamId'] == teamId]
    df = df.loc[df['period'] == period]
    player = df.loc[(df['playerId'] == playerId)]
    defpoints = player[['x', 'y']].values
    print(defpoints)

    fig1, ax = plt.subplots(nrows=1, ncols=1)

    #Create a convex hull object and assign it to the variable hull
    hull = ConvexHull(player[['x', 'y']])
    print(hull)

    #Plot the X & Y location with dots
    fig1.plot(player.x, player.y, 'o')

    #Loop through each of the hull's simplices
    for simplex in hull.simplices:
        #Draw a black line between each
        fig1.plot(defpoints[simplex, 0], defpoints[simplex, 1], 'k-')

    #Fill the area within the lines that we have drawn
    fig1.fill(defpoints[hull.vertices, 0], defpoints[hull.vertices, 1], 'k', alpha=0.3)

    img = fig1.savefig('/assets/generatedPictures/img.png')

    fig = go.Figure()
    pitch = Image.open(img)
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