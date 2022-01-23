import requests
from bs4 import BeautifulSoup


url = 'https://www.python.org/events/python-events'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


headlines2 = soup.find('div', 'most-recent-events').find_all('h3')

for x in headlines2[:]:  
  print(x.text.strip())