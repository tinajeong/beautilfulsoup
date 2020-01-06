from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import re
textf = open("linksource.txt")

while True:
    url = textf.readline()
    if not url: break
    print('source url:\n\t'+url)
    
    # get contents from url
    content = requests.get(url).content
    # get soup
    soup = BeautifulSoup(content,'html.parser') # choose html.parser
    # find the tag : <img ... >
    image_tags = soup.findAll('img')

    # print out image urls
    print("image source list:\n\t")

    source_list = []
    for image_tag in image_tags:
        print(image_tag.get('src'))
        source_list.append(image_tag.get('src'))

    # download image
    for source in source_list:
        file_name= re.sub("[^A-Za-z0-9]*","",source)
        urllib.request.urlretrieve(source, 'images/'+file_name+'.jpg')
    