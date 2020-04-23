import pandas as pd


list_ration = {}
list_ration_two = {}
list_ration_three = {}
list_ration_four = {}


class Ratios:

    def Liquidity(self):
        data = pd.read_pickle("balance_data")

        try:
            I_doc = round(int(data["wartosc"][15]) / int(data["wartosc"][1]), 3)
            list_ration["I stopień pokrycia: "] = I_doc
        except ValueError:
            list_ration["I stopień pokrycia: "] = "brak_danych"
        try:
            II_doc = round((int(data["wartosc"][15]) + int(data['wartosc'][20])) / int(data["wartosc"][1]), 3)
            list_ration["II stopień pokrycia: "] = II_doc
        except ValueError:
            list_ration["II stopień pokrycia: "] = "brak_danych"
        try:
            cash_flow = round(int(data["wartosc"][11]) / int(data["wartosc"][26]), 3)
            list_ration["Płynność gotówkowa: "] = cash_flow
        except ValueError:
            list_ration["Płynność gotówkowa: "] = "brak_danych"
        try:
            fast_liquidity = round(
                (int(data["wartosc"][7]) - int(data["wartosc"][8]) - int(data["wartosc"][32])) / int(
                    data["wartosc"][26]),
                3)
            list_ration["Płynność szybka: "] = fast_liquidity
        except ValueError:
            list_ration["Płynność szybka: "] = "brak_danych"
        try:
            current_liquidity = round(int(data["wartosc"][7]) / int(data["wartosc"][26]), 3)
            list_ration["Płynność bieżąca: "] = current_liquidity
        except ValueError:
            list_ration["Płynność bieżąca: "] = "brak_danych"
        try:
            higher_liquidity = round(int(data["wartosc"][10]) / int(data["wartosc"][26]), 3)
            list_ration["Płynność podwyższona: "] = higher_liquidity
        except ValueError:
            list_ration["Płynność podwyższona: "] = "brak_danych"
        try:
            covering_of_debts = round(int(data["wartosc"][9]) / int(data["wartosc"][26]), 3)
            list_ration["Pokrycie zobowiązań należnościami: "] = covering_of_debts
        except ValueError:
            list_ration["Pokrycie zobowiązań należnościami: "] = "brak_danych"
        try:
            share_capital = round(
                (int(data["wartosc"][7]) - int(data['wartosc'][26])) / (
                            int(data["wartosc"][1]) + int(data["wartosc"][7])),
                3)
            list_ration["Udział kapitału pracującego w aktywach: "] = share_capital
        except ValueError:
            list_ration["Udział kapitału pracującego w aktywach: "] = "brak_danych"

    def Profitability(self):
        data = pd.read_pickle("balance_data")
        data_two = pd.read_pickle("income_statement_data")



        try:
            ROE = round((int(data_two["wartosc"][16]) / int(data["wartosc"][15])) * 100, 3)
            list_ration_two["ROE: "] = ROE
        except ValueError:
            list_ration_two["ROE: "] = "brak_danych"
        try:
            ROA = round((int(data_two["wartosc"][16]) / (int(data["wartosc"][1]) + int(data["wartosc"][7]))) * 100, 3)
            list_ration_two["ROA: "] = ROA
        except ValueError:
            list_ration_two["ROA: "] = "brak_danych"
        try:
            OPM = round((int(data_two["wartosc"][8]) / int(data_two["wartosc"][1])) * 100, 3)
            list_ration_two["Marża zysku operacyjnego: "] = OPM
        except ValueError:
            list_ration_two["Marża zysku operacyjnego: "] = "brak_danych"
        try:
            NPM = round((int(data_two["wartosc"][16]) / int(data_two["wartosc"][1])) * 100, 3)
            list_ration_two["Marża zysku netto: "] = NPM
        except ValueError:
            list_ration_two["Marża zysku netto: "] = "brak_danych"
        try:
            PM = round((int(data_two["wartosc"][5]) / int(data_two["wartosc"][1])) * 100, 3)
            list_ration_two["Marża zysku ze sprzedaży: "] = PM
        except ValueError:
            list_ration_two["Marża zysku ze sprzedaży: "] = "brak_danych"
        try:
            GPM = round((int(data_two["wartosc"][14]) / int(data_two["wartosc"][1])) * 100, 3)
            list_ration_two["Marża zysku brutto: "] = GPM
        except ValueError:
            list_ration_two["Marża zysku brutto: "] = "brak_danych"
        try:
            GPMOS = round(
                ((int(data_two["wartosc"][1]) - int(data_two["wartosc"][2])) / int(data_two["wartosc"][1])) * 100,
                3)
            list_ration_two["Marża zysku brutto ze sprzedaży: "] = GPMOS
        except ValueError:
            list_ration_two["Marża zysku brutto ze sprzedaży: "] = "brak_danych"
        try:
            OPOA = round((int(data_two["wartosc"][8]) / (int(data["wartosc"][1]) + int(data["wartosc"][7]))) * 100, 3)
            list_ration_two["Rentowność operacyjna aktywów: "] = OPOA
        except ValueError:
            list_ration_two["Rentowność operacyjna aktywów: "] = "brak_danych"

    def Cash_flow(self):
        data_two = pd.read_pickle("income_statement_data")
        data_three = pd.read_pickle("cash_flow_data")

        try:
            SONPIOCF = round((int(data_two["wartosc"][16]) / int(data_three["wartosc"][1])) * 100, 3)
            list_ration_three["Udział zysku netto w przepływach operacyjnych: "] = SONPIOCF
        except ValueError:
            list_ration_three["Udział zysku netto w przepływach operacyjnych: "] = "brak_danych"
        try:
            IOIFS = round(
                (int(data_three["wartosc"][3]) / (int(data_three["wartosc"][1]) + int(data_three["wartosc"][5]))) * 100,
                3)
            list_ration_three["Wskaźnik źródeł finansowania inwestycji: "] = IOIFS
        except ValueError:
            list_ration_three["Wskaźnik źródeł finansowania inwestycji: "] ="brak_danych"

    def Debt(self):
        data = pd.read_pickle("balance_data")



        try:
            GD = round(
                (int(data["wartosc"][20]) + int(data["wartosc"][26])) / (
                            int(data["wartosc"][1]) + int(data["wartosc"][7])),
                3)
            list_ration_four["Zadłużenie ogólne: "] = GD
        except ValueError:
            list_ration_four["Zadłużenie ogólne: "] = "brak_danych"
        try:
            IOE = round((int(data["wartosc"][20]) + int(data["wartosc"][26])) / int(data["wartosc"][15]), 3)
            list_ration_four["Zadłużenie kapitału własnego: "] = IOE
        except ValueError:
            list_ration_four["Zadłużenie kapitału własnego: "] = "brak_danych"
        try:
            LTD = round((int(data["wartosc"][20])) / int(data["wartosc"][15]), 3)
            list_ration_four["Zadłużenie długoterminowe: "] = LTD
        except ValueError:
            list_ration_four["Zadłużenie długoterminowe: "] = "brak_danych"
        try:
            DOFA = round((int(data["wartosc"][3])) / int(data["wartosc"][20]), 3)
            list_ration_four["Zadłużenie środków trwałych: "] = DOFA
        except ValueError:
            list_ration_four["Zadłużenie środków trwałych: "] = "brak_danych"
        try:
            COFAWFC = round(
                (int(data["wartosc"][20]) + int(data["wartosc"][15]) + int(data["wartosc"][32])) / int(
                    data["wartosc"][1]),
                3)
            list_ration_four["Pokrycie aktywów trwałych kapitałami stałymi: "] = COFAWFC
        except ValueError:
            list_ration_four["Pokrycie aktywów trwałych kapitałami stałymi: "] = "brak_danych"
        try:
            DOTFS = round((int(data["wartosc"][20]) + int(data["wartosc"][15])) /
                          (int(data["wartosc"][1]) + int(data["wartosc"][7])), 3)
            list_ration_four["Trwałość struktury finansowania: "] = DOTFS
        except ValueError:
            list_ration_four["Trwałość struktury finansowania: "] = "brak_danych"
        try:
            TUOFC = round((int(data["wartosc"][20]) + int(data["wartosc"][26])) /
                          (int(data["wartosc"][7])), 3)
            list_ration_four["Zastosowanie kapitału obcego: "] = TUOFC
        except ValueError:
            list_ration_four["Zastosowanie kapitału obcego: "] = "brak_danych"
        try:
            one = round((int(data["wartosc"][15]) / int(data["wartosc"][1])), 3)
            two = round((int(data["wartosc"][20]) + int(data["wartosc"][26])) / int(data["wartosc"][7]), 3)
            IOTOFS = one / two
            list_ration_four["Wskaźnik ogólnej sytuacji finansowej: "] = IOTOFS
        except ValueError:
            list_ration_four["Wskaźnik ogólnej sytuacji finansowej: "] = "brak_danych"


def start_Ratios():
    r1 = Ratios()
    r1.Liquidity()
    r1.Debt()
    r1.Cash_flow()
    r1.Profitability()

