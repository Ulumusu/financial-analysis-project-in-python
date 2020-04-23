import pandas as pd
import pickle

company_name = "AGORA"


class download_data:

    def __init__(self, company_name):
        self.company_name = company_name

    def balance(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-bilans/" + self.company_name)
        x = 0

        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Wartości niematerialne i prawne":
                        first = df[x][0][1::]
                        second = df[x].columns[-1]
                        third = df[x][second - 1][1:]
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        mega_list = []

        for x in third:
            word = list(str(x))
            for y in range(len(word) - 1):
                if word[y] == "r" or word[y] == "/":
                    del word[y::]
                    break
                elif word[y] == " ":
                    del word[y]
                else:
                    continue
            word_two = "".join(word)
            mega_list.append(word_two)

        mega_set = pd.DataFrame(mega_list)
        mega_set.index += 1
        result = pd.concat([first, mega_set], axis=1, join_axes=[first.index])
        result.columns = ["dane", "wartosc"]
        result.to_csv("balance.csv")
        pickle_out = open("balance_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()

    def income_statement(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-rachunek-zyskow-i-strat/" + self.company_name)
        x = 0

        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Techniczny koszt wytworzenia produkcji sprzedanej":
                        first = df[x][0][1::]
                        second = df[x].columns[-1]
                        third = df[x][second - 1][1:]
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        mega_list = []

        for x in third:
            word = list(str(x))
            for y in range(len(word)):
                if word[y] == " ":
                    del word[y]
                if word[y] == "r" or word[y] == "/":
                    del word[y::]
                    break
                else:
                    continue
            word_two = "".join(word)
            mega_list.append(word_two)
        mega_set = pd.DataFrame(mega_list)
        mega_set.index += 1
        result = pd.concat([first, mega_set], axis=1, join_axes=[first.index])
        result.columns = ["dane", "wartosc"]
        result.to_csv("income_statement.csv")
        pickle_out = open("income_statement_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()

    def cash_flow(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-przeplywy-pieniezne/" + self.company_name)
        x = 0

        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Amortyzacja":
                        first = df[x][0][1::]
                        second = df[x].columns[-1]
                        third = df[x][second - 1][1:]
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        mega_list = []

        for x in third:
            word = list(str(x))
            for y in range(len(word)):
                if word[y] == " ":
                    del word[y]
                if word[y] == "r" or word[y] == "/":
                    del word[y::]
                    break
                else:
                    continue
            word_two = "".join(word)
            mega_list.append(word_two)
        mega_set = pd.DataFrame(mega_list)
        mega_set.index += 1
        result = pd.concat([first, mega_set], axis=1, join_axes=[first.index])
        result.columns = ["dane", "wartosc"]
        result.to_csv("cash_flow.csv")
        pickle_out = open("cash_flow_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()


p1 = download_data(company_name)
p1.balance()
p1.income_statement()
p1.cash_flow()
