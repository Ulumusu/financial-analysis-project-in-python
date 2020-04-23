import dash_core_components as dcc
import dash_html_components as html

from compare_data import *
from css_style import *
from download_data import *
from all_ratios import *

df = pd.read_csv('balance.csv')
df_two = pd.read_csv('income_statement.csv')
df_three = pd.read_csv('cash_flow.csv')


# show menu
def first_start(company):
    start_download_data(company)
    start_compare_data()
    start_Ratios()
    first = []
    first.append(
        html.Div(
            html.H2(children='Obecne sprawozdania finansowe organizacji ' + company, style=title_style)
        )
    )
    first.append(
        dcc.Dropdown(
            id='graph-dropdown',
            options=[
                {'label': 'Bilans', 'value': 'Bilans'},
                {'label': 'Rachunek Zysków i Strat', 'value': 'Rachunek Zysków i Strat'},
                {'label': 'Rachunek Przepływów', 'value': 'Rachunek Przepływów'},
                {'label': 'Płynność', 'value': 'Płynność'},
                {'label': 'Rentowność', 'value': 'Rentowność'},
                {'label': 'Zadłużenie', 'value': 'Zadłużenie'},
                {'label': 'Przepływy pieniężne', 'value': 'Przepływy pieniężne'},
            ],
            value="Bilans"
        )
    )
    first.append(
        html.Div(id='output-container'),
    )

    return first


# generate table for financial document
def generate_table(dataframe, max_rows=10000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +
        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col],
                    style=table_td) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))],
        style=table_td_two)


def generate_table_for_ratios(ratios, max_rows = 1000):
    return html.Table(
        [html.Tr([
            html.Td(list(ratios.keys())[i] + str(list(ratios.values())[i])
            )
        ]) for i in range(min(len(ratios), max_rows))],
    )


# show graphs on website
def output_graph(value):
    df = pd.read_csv('balance.csv')
    df_two = pd.read_csv('income_statement.csv')
    df_three = pd.read_csv('cash_flow.csv')
    graph = []

    if value == "Bilans":
        graph.append(
            html.Div(
                dcc.Graph(
                    id='Bilans',
                    figure={
                        'data': [
                            {'x': list(fixed_assets.keys()), 'y': list(fixed_assets.values()),
                             'type': 'bar', 'name': 'Aktywa trwałe'},
                            {'x': list(current_assets.keys()), 'y': list(current_assets.values()),
                             'type': 'bar', 'name': 'Aktywa obrotowe'},
                            {'x': list(total_assets.keys()), 'y': list(total_assets.values()),
                             'type': 'bar', 'name': 'Aktywa razem'},
                            {'x': list(equity.keys()), 'y': list(equity.values()),
                             'type': 'bar', 'name': 'Kapitał własny'},
                            {'x': list(long_term_liabilities.keys()), 'y': list(long_term_liabilities.values()),
                             'type': 'bar', 'name': 'Zobowiązania długoterminowe'},
                            {'x': list(short_term_liabilities.keys()), 'y': list(short_term_liabilities.values()),
                             'type': 'bar', 'name': 'Zobowiązania krótkoterminowe'},
                            {'x': list(total_liabilities.keys()), 'y': list(total_liabilities.values()),
                             'type': 'bar', 'name': 'Zobowiązania razem'}
                        ],
                        'layout': {
                            'title': 'Bilans porównanie z poprzednimi latami'
                        }
                    },
                )
            )
        ),
        graph.append(
            html.Div(
                html.H2(children='Bilans', style=title_style),
            ),
        )
        graph.append(
            generate_table(df)
        )
    elif value == "Rachunek Zysków i Strat":
        graph.append(
            html.Div(
                dcc.Graph(
                    id='Rachunek Zysków i Strat',
                    figure={
                        'data': [
                            {'x': list(Net_revenues_from_sales.keys()),
                             'y': list(Net_revenues_from_sales.values()),
                             'type': 'bar', 'name': 'Przychody ze Sprzedaży'},
                            {'x': list(Gross_profit_on_sales.keys()),
                             'y': list(Gross_profit_on_sales.values()),
                             'type': 'bar', 'name': 'Zysk ze sprzedaży'},
                            {'x': list(Profit_on_operating_activities.keys()),
                             'y': list(Profit_on_operating_activities.values()),
                             'type': 'bar', 'name': 'Zysk operacyjny (EBIT)'},
                            {'x': list(Profit_on_business_activities.keys()),
                             'y': list(Profit_on_business_activities.values()),
                             'type': 'bar', 'name': 'Zysk z działalności gospodarczej)'},
                            {'x': list(Gross_profit.keys()),
                             'y': list(Gross_profit.values()),
                             'type': 'bar', 'name': 'Zysk Brutto'},
                            {'x': list(Net_profit.keys()),
                             'y': list(Net_profit.values()),
                             'type': 'bar', 'name': 'Zysk Netto'}
                        ],
                        'layout': {
                            'title': 'Rachunek Zysków porównanie z poprzednimi latami'
                        }
                    },
                )
            )
        ),
        graph.append(
            html.Div(
                html.H2(children='Rachunek Zysków i Strat', style=title_style),
            )
        )
        graph.append(
            generate_table(df_two)
        )
    elif value == "Rachunek Przepływów":
        graph.append(
            html.Div(
                dcc.Graph(
                    id='Rachunek Przepływów',
                    figure={
                        'data': [
                            {'x': list(Cash_flows_from_operating_activities.keys()),
                             'y': list(Cash_flows_from_operating_activities.values()),
                             'type': 'bar', 'name': 'Przepływy pieniężne z działalności operacyjnej'},
                            {'x': list(Cash_flows_from_investment_activities.keys()),
                             'y': list(Cash_flows_from_investment_activities.values()),
                             'type': 'bar', 'name': 'Przepływy pieniężne z działalności inwestycyjnej'},
                            {'x': list(Cash_flows_from_financial_activities.keys()),
                             'y': list(Cash_flows_from_financial_activities.values()),
                             'type': 'bar', 'name': 'Przepływy pieniężne z działalności finansowej'},
                            {'x': list(Total_net_cash_flows.keys()),
                             'y': list(Total_net_cash_flows.values()),
                             'type': 'bar', 'name': 'Przepływy pieniężne razem'},
                        ],
                        'layout': {
                            'title': 'Rachunek Przepływów porównanie z poprzednimi latami'
                        }
                    },
                )
            )
        ),
        graph.append(
            html.Div(
                html.H2(children='Rachunek Przepływów pieniężnych', style=title_style),
            )
        ),
        graph.append(
            generate_table(df_three)
        )
    elif value == "Płynność":
        graph.append(
            generate_table_for_ratios(list_ration)
        )
    elif value == "Rentowność":
        graph.append(
            generate_table_for_ratios(list_ration_two)
        )
    elif value == "Zadłużenie":
        graph.append(
            generate_table_for_ratios(list_ration_four)
        )
    elif value == "Przepływy pieniężne":
        graph.append(
            generate_table_for_ratios(list_ration_three)
        )
    return graph
