from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore
import sys
import pandas as pd # type: ignore

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

sys.stdout.reconfigure(encoding="utf-8")


table = doc.find_all('table')[1]


table_headers = table.find_all('th')
table_header_titles = [header.text.strip() for header in table_headers]  

data = table.find_all('tr')
all_rows = []
for row in data:
    row_data = row.find_all('td')
    individual_row = [data.text.strip() for data in row_data]
    if individual_row:
        all_rows.append(individual_row)  

df = pd.DataFrame(all_rows,columns=table_header_titles[:len(all_rows[0])])
length = len(df)
df.loc[length] = individual_row

print(df)

df.to_csv(r"D:\Projects\Web scrapping\Automobiles\Data.csv",index=False)
print(df)
