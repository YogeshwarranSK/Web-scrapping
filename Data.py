from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import sys 

url = f"https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url).text # Collecting the data as text from url
doc = BeautifulSoup(page,"html.parser")

# To convert data to utf-8 format
sys.stdout.reconfigure(encoding="utf-8")

#print(doc.prettify())

table = doc.find_all('table')[0]

# To exctract table heading
table_header = table.find_all('th')
table_header_title = [title.text.strip() for title in table_header]

# To exctract table rows
column_data = table.find_all('tr')

# To extract all data into list
all_rows = []  

for row in column_data[1:]:  # Iterating over table rows
    row_data = row.find_all('td')
    individual_row = [data.text.strip() for data in row_data]
    if individual_row:
        all_rows.append(individual_row)  

import pandas as pd # type: ignore

# Convert data to dataframes
df = pd.DataFrame(all_rows,columns=table_header_title)
length = len(df)
df.loc[length] = individual_row

# Convert dataframe to csv format
df.to_csv(r"D:\Projects\American Data\Output.csv", index=False)
print(df)











