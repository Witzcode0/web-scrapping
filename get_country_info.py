import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_excel('world_population_data.xlsx')

get_countries = df[['no', 'name', 'link']]

for country in get_countries.iterrows():
    no = country[1][0]
    name = country[1][1]
    link = country[1][2]
    print(no, name, link)
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find_all('table', attrs={"class":"table"})[-1]
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        cities = []
        for row in rows:
            city = {}
            tds = list(row.find_all('td'))
            city['no']=tds[0].text
            city['name']=tds[1].text
            city['population']=tds[2].text
            cities.append(city)
        df = pd.DataFrame(cities)
        df.to_excel(f'country/{no}_{name}_.xlsx', index=False)
    