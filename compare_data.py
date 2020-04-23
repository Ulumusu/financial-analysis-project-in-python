import pandas as pd
import datetime
time = datetime.datetime.now()

# balance dictionary
fixed_assets = {}
current_assets = {}
total_assets = {}
equity = {}
long_term_liabilities = {}
short_term_liabilities = {}
total_liabilities = {}

# income statement dictionary
Net_revenues_from_sales = {}
Gross_profit_on_sales = {}
Profit_on_operating_activities = {}
Profit_on_business_activities = {}
Gross_profit = {}
Net_profit = {}

# cash flow dictionary
Cash_flows_from_operating_activities = {}
Cash_flows_from_investment_activities = {}
Cash_flows_from_financial_activities = {}
Total_net_cash_flows = {}


class compare_data:

    def balance(self):
        data = pd.read_csv("balance.csv")
        years =[data[data.columns[2]], data[data.columns[3]], data[data.columns[4]]]

        number = 2
        for year in years:
            word = list(str(data.columns[number]))
            for y in range(len(word)):
                if word[y] == "/":
                    del word[y::]
                    break
                else:
                    continue
            word_two = "".join(word)
            fixed_assets[word_two] = year[0]
            current_assets[word_two] = year[6]
            total_assets[word_two] = year[13]
            equity[word_two] = year[14]
            long_term_liabilities[word_two] = year[19]
            short_term_liabilities[word_two] = year[25]
            total_liabilities[word_two] = year[32]
            number += 1

    def income_statement(self):
        data = pd.read_csv("income_statement.csv")
        years = [data[data.columns[2]], data[data.columns[3]], data[data.columns[4]]]

        number = 2
        for year in years:
            word = list(str(data.columns[number]))
            for y in range(len(word)):
                if word[y] == "/":
                    del word[y::]
                    break
                else:
                    continue
            word_two = "".join(word)
            change_year = word_two.split(" ")
            for z in change_year:
                if z == 'O4K' or z == 'O1K' or z == 'O3K' or z == 'O2K':
                    word_two = str(time.year)
                    break
            Net_revenues_from_sales[word_two] = year[0]
            Gross_profit_on_sales[word_two] = year[4]
            Profit_on_operating_activities[word_two] = year[7]
            Profit_on_business_activities[word_two] = year[11]
            Gross_profit[word_two] = year[13]
            Net_profit[word_two] = year[15]
            number += 1

    def cash_flow(self):
        data = pd.read_csv("cash_flow.csv")
        years = [data[data.columns[2]], data[data.columns[3]], data[data.columns[4]]]

        number = 2
        for year in years:
            word = list(str(data.columns[number]))
            for y in range(len(word)):
                if word[y] == "/":
                    del word[y::]
                    break
                else:
                    continue
            word_two = "".join(word)
            change_year = word_two.split(" ")
            for z in change_year:
                if z == 'O4K' or z == 'O1K' or z == 'O3K' or z == 'O2K':
                    word_two = str(time.year)
                    break
            Cash_flows_from_operating_activities[word_two] = year[0]
            Cash_flows_from_investment_activities[word_two] = year[2]
            Cash_flows_from_financial_activities[word_two] = year[4]
            Total_net_cash_flows[word_two] = year[7]
            number += 1


def start_compare_data():
    c1 = compare_data()
    c1.balance()
    c1.income_statement()
    c1.cash_flow()


start_compare_data()








