import pandas as pd
import pickle


class download_data():

    def __init__(self, company_name):
        self.company_name = company_name

    # download data from balance
    def balance(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-bilans/" + self.company_name)
        x = 0
        # check and download data from correct table for last three years included current
        list_with_data = []
        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Wartości niematerialne i prawne":
                        name = df[x][0][1::]
                        number_of_years = df[x].columns[-1]
                        current_year = df[x][number_of_years - 1][0:]
                        last_year = df[x][number_of_years - 2][0:]
                        reverse_year = df[x][number_of_years - 3][0:]
                        list_with_data.extend((current_year, last_year, reverse_year))
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        year_list = {}
        # cleared string, numbers for ratios
        for year in list_with_data:
            mega_list = []
            name_of_year = year[0]
            year = year[1:]
            for x in year:
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
            year_list[name_of_year] = mega_list
        # save data, numbers in pickle format
        mega_set = pd.DataFrame(list(year_list.values())[0])
        mega_set_two = pd.DataFrame(list(year_list.values())[1])
        mega_set_three = pd.DataFrame(list(year_list.values())[2])
        mega_set.index += 1
        mega_set_two.index += 1
        mega_set_three.index += 1
        result = pd.concat([name, mega_set], axis=1, join_axes=[name.index])
        result.columns = ["dane", "wartosc"]
        pickle_out = open("balance_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()
        # save data in csv format
        result_to_compare = pd.concat([name, mega_set, mega_set_two, mega_set_three],
                                      axis=1, join_axes=[name.index])
        result_to_compare.columns = ["dane", str(list(year_list.keys())[0]),
                                     str(list(year_list.keys())[1]),
                                     str(list(year_list.keys())[2])]
        result_to_compare.to_csv("balance.csv")

    # download data from income_statement
    def income_statement(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-rachunek-zyskow-i-strat/" + self.company_name)
        x = 0

        list_with_data = []
        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Techniczny koszt wytworzenia produkcji sprzedanej":
                        name = df[x][0][1::]
                        number_of_years = df[x].columns[-1]
                        current_year = df[x][number_of_years - 1][0:]
                        last_year = df[x][number_of_years - 2][0:]
                        reverse_year = df[x][number_of_years - 3][0:]
                        list_with_data.extend((current_year, last_year, reverse_year))
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        year_list = {}

        for year in list_with_data:
            mega_list = []
            name_of_year = year[0]
            year = year[1:]
            for x in year:
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
            year_list[name_of_year] = mega_list

        mega_set = pd.DataFrame(list(year_list.values())[0])
        mega_set_two = pd.DataFrame(list(year_list.values())[1])
        mega_set_three = pd.DataFrame(list(year_list.values())[2])
        mega_set.index += 1
        mega_set_two.index += 1
        mega_set_three.index += 1
        result = pd.concat([name, mega_set], axis=1, join_axes=[name.index])
        result.columns = ["dane", "wartosc"]
        pickle_out = open("income_statement_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()

        result_to_compare = pd.concat([name, mega_set, mega_set_two, mega_set_three],
                                      axis=1, join_axes=[name.index])
        result_to_compare.columns = ["dane", str(list(year_list.keys())[0]),
                                     str(list(year_list.keys())[1]), str(list(year_list.keys())[2])]
        result_to_compare.to_csv("income_statement.csv")

    # download data from cash_flow
    def cash_flow(self):
        df = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-przeplywy-pieniezne/" + self.company_name)
        x = 0

        list_with_data = []
        while x <= 4:
            if x == 4:
                break
            else:
                try:
                    if df[x][0][2] == "Amortyzacja":
                        name = df[x][0][1::]
                        number_of_years = df[x].columns[-1]
                        current_year = df[x][number_of_years - 1][0:]
                        last_year = df[x][number_of_years - 2][0:]
                        reverse_year = df[x][number_of_years - 3][0:]
                        list_with_data.extend((current_year, last_year, reverse_year))
                        break
                except KeyError:
                    pass
                if x == 4:
                    break
                else:
                    x += 1

        year_list = {}

        for year in list_with_data:
            mega_list = []
            name_of_year = year[0]
            year = year[1:]
            for x in year:
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
            year_list[name_of_year] = mega_list

        mega_set = pd.DataFrame(list(year_list.values())[0])
        mega_set_two = pd.DataFrame(list(year_list.values())[1])
        mega_set_three = pd.DataFrame(list(year_list.values())[2])
        mega_set.index += 1
        mega_set_two.index += 1
        mega_set_three.index += 1
        result = pd.concat([name, mega_set], axis=1, join_axes=[name.index])
        result.columns = ["dane", "wartosc"]
        pickle_out = open("cash_flow_data", "wb")
        pickle.dump(result, pickle_out)
        pickle_out.close()

        result_to_compare = pd.concat([name, mega_set, mega_set_two, mega_set_three],
                                      axis=1, join_axes=[name.index])
        result_to_compare.columns = ["dane", str(list(year_list.keys())[0]),
                                     str(list(year_list.keys())[1]), str(list(year_list.keys())[2])]
        result_to_compare.to_csv("cash_flow.csv")


company_name = "AGORA"


def start_download_data(company_name):
    d1 = download_data(company_name)
    d1.balance()
    d1.cash_flow()
    d1.income_statement()


start_download_data(company_name)
