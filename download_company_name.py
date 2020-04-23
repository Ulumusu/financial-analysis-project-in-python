import pandas as pd

list_of_company = []

class download_company_name:

    global df
    df = pd.read_html("https://www.biznesradar.pl/gielda/akcje_gpw")

    def only_name(self):
        data = df[0][0]
        for company in data:
            if company == "Profil":
                del(company)
            else:
                start = "("
                end = ")"
                start_index = company.find(start)
                end_index = company.find(end)
                list_of_company.append(company[start_index+1:end_index])


dc1 = download_company_name()
dc1.only_name()
