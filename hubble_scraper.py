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
    sub_reqs = requests.get(sub_url)
    sub_soup = BeautifulSoup(sub_reqs.text, 'html.parser')
    time.sleep(1)
    
    print(sub_url)

    for link in sub_soup.find_all('a', href=True, string='Large JPEG'):
        print(link.get('href'))


#sub_url = 'https://esahubble.org/images/heic2018b/'
#reqs = requests.get(url)
#soup = BeautifulSoup(reqs.text, 'html.parser')
#links = soup.find_all('a href="https://cdn.esahubble.org/archives/images/large')

#for link in soup.find_all('a', href=True, string='Large JPEG'):
#    print(link.get('href'))