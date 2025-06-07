import requests
from bs4 import BeautifulSoup
import os

for i in range(37):

    url = "https://esahubble.org/images/archive/category/galaxies/page/" + str(i + 1)
    r  = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.text + " page: " + str(i + 1))