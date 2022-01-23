import requests
from bs4 import BeautifulSoup


url = 'https://www.python.org'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


headlines2 = soup.find('div', 'medium-widget event-widget last').find_all('li')

for x in headlines2:  
  print(x.text.strip())
  print()
