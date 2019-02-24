from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

# sapo = "https://casa.sapo.pt/Venda/Apartamentos/?sa=11&or=10"
url1 = "https://ingatlan.com/lista/elado+haz+torokbalint+30-50-mFt+60-m2-felett"

response = get(url1, headers=headers)

# print(response)
# print(response.text[:100])

html_soup = BeautifulSoup(response.text, 'html.parser')

# ingatlan.com
ingatlan_containers = html_soup.find_all('div', class_="listing__card")

# eddig okés 20 találat/oldal
print(len(ingatlan_containers))

first = ingatlan_containers[0]
first.find_all('price')



