import requests
from bs4 import BeautifulSoup
import os

url = input('Provide url: \n')

r requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(soup.title.text)