import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={"id":"example2"})
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')
    countries = []
    for row in rows:
        country_data = {}
        tds = list(row.find_all('td'))
        country_data['no'] = tds[0].text
        country_data['name'] = tds[1].text
        country_data['link'] = 'https://www.worldometers.info' + str(tds[1].find('a')['href'])
        country_data['population']  = tds[2].text
        country_data['land-aria'] = tds[4].text
        countries.append(country_data)
        print(country_data)
    # Create a DataFrame from the array of dictionaries
    df = pd.DataFrame(countries)

    # Save the DataFrame to an Excel file
    df.to_excel('population_data.xlsx', index=False)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")