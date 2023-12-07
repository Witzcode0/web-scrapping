import pandas as pd

wpd = pd.read_excel('world_population_data.xlsx')
# print(wpd['name'].tolist())
cf = pd.read_excel('country_flag.xlsx')
# print(cf['country'].tolist())

# Convert elements to lowercase and find common elements
common_elements = set(map(str.lower, wpd['name'].tolist())).intersection(map(str.lower, cf['country'].tolist()))

# Alternatively, using set intersection operator
# common_elements = set(map(str.lower, list1)) & set(map(str.lower, list2))

# Convert the result back to a list if needed
common_elements_list = list(common_elements)

print("Common elements (case-insensitive):", len(common_elements_list))