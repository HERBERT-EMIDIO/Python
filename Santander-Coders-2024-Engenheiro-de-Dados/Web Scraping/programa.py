import requests 
html = requests.get("https://history.state.gov/countries/all")

from bs4 import BeautifulSoup
html_parsed = BeautifulSoup(html, "html.parser")

html_parsed

print(html_parsed.prettify())

# Buscar as Class com nomes dos países 

html_parsed.find(class_ = "row").text.strip()

# loop
list_paises = html_parsed.find_all(class_ = "contry-name")
list_capitais = html_parsed.find_all(class_ = "contry-capital")

lista_final = []

for pais,capital in zip(list_capitais):
    dici = {'pais': pais.text.strip(),
             "capital":capital.text.strip()               
            }
    
    lista_final.append(dici)