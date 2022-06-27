from cProfile import Profile
from pstats import Stats
from pydoc import classname
from turtle import position, width
from unicodedata import name
import dash
from dash import dcc
from dash import Dash, html, dcc, Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from dash import Dash, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import dash_daq as daq
import joblib


########Initialize app#######
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)
app.title = "Class Quiz Dashboard"
server = app.server


########Load data#######
df = (pd.read_csv('Webdata_PlayerType.csv')).iloc[:200]


########Figures #######


########Dash App Components#######

logo = html.A(
    [
        html.Img(
            src=app.get_asset_url("logo_classquiz.png"), height="90px"),

    ], className="logo",
)

id_filter = dbc.Card(
    dbc.CardBody(
        [html.Label("Select By user ID:"),
         html.Br(),
         dcc.Dropdown(
            df.id.unique(),
            id="input_id",
        ),

        ], className='filter',
    )
)

name_filter = dbc.Card(
    dbc.CardBody(
        [html.Label("Select By user NAME:"),
         html.Br(),
         dcc.Dropdown(
            id="Name",
            # df.name.unique(),
            value="level_id",
        ),
        ], className='filter',
    )
)

filters = dbc.Row(
    [
        dbc.Col(id_filter, width=4),
        dbc.Col(name_filter, width=4,
                ),
    ], justify="between",
)

Profile = dbc.Card(
    [
        html.P("User ID :"),
        html.P("Full Name :"),
        html.P("Level of Study:"),
        html.P("Completed Execices:"),
    ],
    className="profile"
)

Progress = html.Div(

    [
        html.P("Execellence", className="progress_title"),
        dbc.Progress(value=25, max=100,
                     className='progress_bar', color="warning"),

        html.P("Concentration", className="progress_title"),
        dbc.Progress(value=45, max=100,
                     className='progress_bar', color="danger"),

        html.P("Sucess", className="progress_title"),
        dbc.Progress(value=70, max=100,
                     className='progress_bar', color="info"),

    ], style={
        'padding': '22px'
    }
)

Player_type = dbc.Card(
    [
        html.H4("Player Type"),

    ], className='card_playerType',
)

Intelligence_type = dbc.Card(
    [
        html.H4("Intelligence Type"),
    ], className='card_intelligenceType',
)

Troube = dbc.Card(
    [
        html.H4("Truble"),
    ], className='card_troubleType',
)

Candy = dbc.Card(
    [
        html.H4("Candy"),
    ], className='card_candy',
)

Donuts = dbc.Card(
    [html.H4("Donuts"),
     ], className='card_donuts',
)

Stats = dbc.Row(
    [dbc.Col(Player_type, width=3),
     dbc.Col(Intelligence_type, width=3),
     dbc.Col(Troube, width=3),
     dbc.Col(
        [dbc.Row(Candy),
         dbc.Row(Donuts), ], width=3
    ),
    ],
)

Profile_progress = dbc.Row(
    [dbc.Col(Profile, width=4),
        dbc.Col(Progress)

     ],)


########Dash App Layout #######

app.layout = dbc.Container(
    [logo,
        filters,
        Profile_progress,
        Stats

     ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True, port=50)
