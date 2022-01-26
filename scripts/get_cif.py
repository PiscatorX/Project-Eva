#!/usr/bin/env  python 
from bs4  import  BeautifulSoup
from urllib.parse import urlparse
import itertools as it
import requests
import time




url= "http://www.hypotheticalzeolites.net./dataconfirmed?page={}&ent_pp={}&orderby=bgbener&toggle=-asc"

print(urlparse)

def select(link, tag = "viewer"):
  
    if tag in link:
        return print(link)
    else:
        return False



data =  open("page.html").read().splitlines()

for link in data:
    if select(link):
        print(link)



    









# entries = 200
# i  =  0
# for page in it.count(start=1):
    
#     zeoliteDB_url  = url.format(page,entries)
#     req = requests.get(zeoliteDB_url)
#     soup = BeautifulSoup(req.text, "html.parser")

#     for link in soup.find_all('a'): 
#         print(link.get('href'))
        
#     break

# soup = BeautifulSoup(request.text, "html.parser")
# for link in  soup.findall('a'):
#     print(link)
 
