import re
import time
import requests
from bs4 import BeautifulSoup

url = 'https://esahubble.org/images/archive/category/galaxies/page/1/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
image_script = soup.find('script')
image_links = re.findall(r"url\s*:\s*'([^']+)'", str(image_script))

for links in image_links:
    sub_url = "https://esahubble.org" + links
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    time.sleep(1)
    print(sub_url)