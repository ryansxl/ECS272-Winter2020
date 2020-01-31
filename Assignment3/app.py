import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import urllib.request as req
from dash.dependencies import Input, Output
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dataset = req.urlopen('http://stream.cs.ucdavis.edu/datasets/LAX_Terminal_Passengers.csv')
data = pd.read_csv(dataset)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

terminal0= data['Terminal'].unique().tolist()
arrivals= data['Arrival_Departure'].unique().tolist()
domestics= data['Domestic_International'].unique().tolist()
months=[1,2,3,4,5,6,7,8,9,10,11,12]



app.layout = html.Div([
    html.H1('ECS272 Assignment 3 ---- Xinlin Shuai'),
    html.H2('Basic visualization'),
    html.Br(),
    dcc.Graph(id='line'),
    dcc.Dropdown(id='year',options=[
        {'label':i,'value':i} for i in range (2006,2019)],
        value = 2006
        ),
    dcc.Dropdown(id='terminal',options=[
        {'label': terminal00,'value':terminal00} for terminal00 in terminal0],
        value = 'Terminal 1'
        ),
    html.Br(),
    dcc.Graph(id='sankey'),
    dcc.Dropdown(id='year2',options=[
        {'label':i,'value':i} for i in range (2006,2019)],
        value = 2006
        ),
    ]
,style={'textAlign': 'center'})

@app.callback(
    [Output('line','figure'),
     Output('sankey','figure')],
    [Input('year','value'),
     Input('terminal','value'),
     Input('year2','value')]
    )
def update_figure(selected_year,selected_terminal,selected_year2):


    filtered_data = data[data['ReportPeriod'].str.slice(start=6, stop=10) == (str(year))][['ReportPeriod','Terminal', 'Domestic_International', 'Arrival_Departure']]
    figure = px.parallel_categories(filtered_df, dimensions_max_cardinality = 12)
    return figure
    
    return{
        
        }



if __name__ == '__main__':
    app.run_server(debug=True)
