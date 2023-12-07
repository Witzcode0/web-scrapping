import pandas as pd

df = pd.read_json('country_flag.json')
df.to_excel('country_flag.xlsx', index=False)
