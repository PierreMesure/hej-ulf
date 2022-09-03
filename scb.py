import string
import requests
import pandas as pd

URL = 'https://www.scb.se/contentassets/5a07e6b5601f49ffbb1f31a14d0ad59f/namn-med-minst-tva-barare-31-december-2021_20220404.xlsx'

class SCB(object):

    @staticmethod
    def fetch_names(amount):
        print(f'Fetching names from SCB')

        file = pd.ExcelFile(requests.get(URL).content)
        #file = pd.ExcelFile('namn-scb.xlsx')

        print(f'Fetched names from SCB')
        df_men = pd.read_excel(file, 'Förnamn män', skiprows=4)
        df_women = pd.read_excel(file, 'Förnamn kvinnor', skiprows=4)

        df = pd.concat([df_men, df_women])
        df = df.sort_values('Antal bärare', ascending=False).dropna()
        df = df.head(amount)['Förnamn']

        return list(map(string.capwords, df.to_list()))
