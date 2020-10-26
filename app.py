# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:59:07 2020

@author: vera.meinert
"""

# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

filename = 'Beispiel_Daten.csv'
df = pd.read_csv(filename, sep = ';', index_col = 'index')


fig = px.bar(df, 
             x='Business Unit', 
             y='M-Level',
             hover_name='Use Case Title',
             hover_data={'Tools': True, 
                         'Use Case Description': True,
                         'Business Unit':False,
                         'M-Level': False,
                         'Use Case Title': False}, 
             color='Use Case Title',
             labels={'pop':'population of Canada'}, 
             height=450, 
             barmode="group",
             text='Use Case Title',
             color_discrete_sequence= ['rgb(37,179,195)', 
                                       'rgb(37,0,68)', 
                                       'rgb(252,186,40)',
                                       'rgb(255,0,68)'],
             )



header_image_source = 'C:/Users/vera.meinert/OneDrive - MAYATO GMBH/Dokumente/Projekte/Untitled Folder/Speed_dating.PNG'
header_image_height = 80
header_image_width = 2 * header_image_height

colors = {
    'background': '#FCF7EF',
    'text': '#FF0044',
    'highlight': '25B3C3'
}

app.layout = html.Div(children=[
    html.Img(
            style={"margin-right": 10},
            src = app.get_asset_url("PTC_logo.png"),
            height = header_image_height,
            width = header_image_width
            ),
    html.H1(
            children='AI Maturity Check',
            style={
                'textAlign': 'center',
                'color': colors['text']
                }),
    
    html.Div(
            children='This Application shows you how mature your first Use Cases are.', 
            style={
                'textAlign': 'center',
                'color': colors['text']
                }),
     dcc.Graph(
        id='AI Maturity Check',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)