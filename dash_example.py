import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

#load dataset
df = pd.read_csv("datasets/europaFinal.csv")
df.head()