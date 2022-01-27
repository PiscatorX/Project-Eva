#!/usr/bin/env  python 
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import itertools as it
import constant
import requests
import time
import sys
import os



def scrape_website(total_entries, start_page = 1, page_limit = 200,  relpath = "hypotheticalzeolite", log = ".zeo_history"):

    logfile = os.path.join(relpath,log)
    if os.path.exists(logfile):
        history =  tuple(open(logfile).read().splitlines())
    else:
        history = tuple()
    url = constant.CONFIRMED_DATA_URL
    url_p = urlparse(url)
    
    entry_counter  = 0    
    for page in it.count(start=start_page):
        url  = url.format(page, page_limit)
        for link1 in get_elements(url, 'a', 'href'):
            time.sleep(1)
            if "viewer" in link1:
                follow = "".join([url_p.scheme+"://", url_p.netloc, link1])
                cif_fname = urlparse(follow).query.split("=")[1]
                if cif_fname in history:
                    continue
                for link2 in get_elements(follow, 'a', None):
                    time.sleep(1)
                    if link2.string == "CIF file":
                        rel_soup = BeautifulSoup(str(link2), 'html.parser')
                        cif_link =   "".join([url_p.scheme+"://", url_p.netloc, rel_soup.a['href']])
                        save2disk(cif_link, cif_fname, logfile, relpath)
                        entry_counter += 1
                        if entry_counter == 5:
                            sys.exit(0)
                        time.sleep(5)
                        
                        
    
def get_elements(url, element, attrib):

    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    if attrib:
        return [ link.get(attrib) for link in soup.find_all(element) ]
    else:
        return [ link for link in soup.find_all(element) ]


    
def save2disk(cif_link, cif_fname, logfile, relpath):
    
    if not os.path.exists(relpath):
         os.mkdir(relpath)
         
    cif_path = os.path.join(relpath, cif_fname)
    cif_data = urlopen(cif_link)
    with open(cif_path, 'wb') as cif_fobj:
        cif_fobj.write(cif_data.read())

    log_fobj = open(logfile, 'a+')
    print(cif_path)
    print(cif_fname, file=log_fobj)  




    
if __name__  ==  "__main__":
    scrape_website(total_entries =  5)    
    
