import dash
from dash import dcc, callback, Output, Input, dash_table
# import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px

# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SOLAR],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

server = app.server
