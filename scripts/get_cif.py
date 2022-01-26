#!/usr/bin/env  python 
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import itertools as it
import constant
import requests
import pprint
import time
import sys
import os



def scrape_website(start_page = 1, entries = 200, relpath = "hypotheticalzeolite", log = ".zeo_history"):

    logfile = os.path.join(relpath,log)
    if os.path.exists(relpath):
        history =  tuple(open(logifle).read().splitlines())
    else:
        history = tuple()
    url = constant.CONFIRMED_DATA_URL
    url_p = urlparse(url)
    for page in it.count(start=start_page):
        url  = url.format(page,entries)
        for link1 in get_elements(url, 'a', 'href'):
            if "viewer" in link1:
                follow = "".join([url_p.scheme+"://", url_p.netloc, link1])
                cif_fname = urlparse(follow).query.split("=")[1]
                if cif_fname in history:
                    continue
                for link2 in get_elements(follow, 'a', None):
                    if link2.string == "CIF file":
                        rel_soup = BeautifulSoup(str(link2), 'html.parser')
                        cif_link =   "".join([url_p.scheme+"://", url_p.netloc, rel_soup.a['href']])
                        save2disk(cif_link, cif_fname, logfile)
                        time.sleep(5)
        
                        
    
def get_elements(url, element, attrib):

    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    if attrib:
        return [ link.get(attrib) for link in soup.find_all(element) ]
    else:
        return [ link for link in soup.find_all(element) ]


    
def save2disk(cif_link, cif_name, logfile  ):
    
    
    cif_data = urlopen(download)
    if not os.path.exists(relpath):
         os.mkdir(relpath)
         
    cif_path = os.path.join(relpath, cfname)
    with open(cif_path, 'w') as cif_fobj:
        cif_fobj.write(cif_data.read())

    log_fobj = open(logfile, 'a+')
    sys.stdout.write(cif_path)
    print(cif_name, file=logfile)  

    
scrape_website(start_page = 1, entries = 200)    
    
