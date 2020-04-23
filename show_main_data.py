import dash
from graph_and_table import *

app = dash.Dash()
app.config['suppress_callback_exceptions']=True
app.layout = html.Div([

    html.H2(children='Wybierz spółkę akcyjną '),
    dcc.Input(
        id = "company_name",
        placeholder='Dodaj spółkę...',
        type='text',
        value=''
    ),
    html.Div(id = "first-data"),
])


@app.callback(
    dash.dependencies.Output('first-data', 'children'),
    [dash.dependencies.Input('company_name', 'value')])
def update_company(value):
    return first_start(value.upper())


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('graph-dropdown', 'value')])
def update_output_graph(value):
    return output_graph(value)


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False, dev_tools_props_check=False)


