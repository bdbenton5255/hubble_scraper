import re
import requests
from bs4 import BeautifulSoup

url = 'https://esahubble.org/images/archive/category/galaxies/page/1/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
image_script = soup.find('script')
image_links = re.findall(r"/images/*", str(image_script))

print(image_links)