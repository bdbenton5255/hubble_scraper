import re
import os
import time
import urllib
import requests
import urllib.request
from bs4 import BeautifulSoup

try:
    os.mkdir("galaxy_images")
except FileExistsError:
    print("galaxy_images directory already exists.")


url = 'https://esahubble.org/images/archive/category/galaxies/page/1/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
image_script = soup.find('script')
image_links = re.findall(r"url\s*:\s*'([^']+)'", str(image_script))
image_number = 0

for links in image_links:

    sub_url = "https://esahubble.org" + links
    sub_reqs = requests.get(sub_url)
    sub_soup = BeautifulSoup(sub_reqs.text, 'html.parser')
    time.sleep(1)
    
    print("Image page: " + str(sub_url))

    for link in sub_soup.find_all('a', href=True, string='Large JPEG'):
        
        high_res_image_link = link.get('href')
        print("Large JPEG link: " + str(high_res_image_link))

        time.sleep(1)

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(high_res_image_link, "galaxy_images/galaxy_" + str(image_number) +".jpg")

        print("Image " + "galaxy_" + str(image_number) + ".jpg downloaded!")
        image_number += 1