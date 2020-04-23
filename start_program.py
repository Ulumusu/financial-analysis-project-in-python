import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from download_data import *
from graph_and_table import *

app = dash.Dash()

app.layout = html.Div(children=[
    # comparision dropdown menu
    dcc.Input(id='my-id', value='RAWLPLUG', type='text'),
    html.Div(id='my-div')
    ])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    company_name = input_value
    start_download_data(str(company_name))
    start_compare_data()
    value = "Bilans"
    generate_table(df)
    return