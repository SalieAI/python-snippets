'''
short snippet to use BeautifulSoup for getting urls  from website and more
'''

import requests
from bs4 import BeautifulSoup

header ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}

def make_soup(url)

    '''
    function which will return bs4 object from url
    '''
    
    r = requests.get(url, headers = header)
    return BeautifulSoup(r.text, 'lxml')

def find_links(url)

    '''
    function which will return urls and theirs name in nested list from url
    '''
    
    r = requests.get(url, headers = header)
    soup = BeautifulSoup(r.text, 'lxml')
    links = soup.findAll('a', href = 'True')
    if links:
        return [(item['href'], item.text) for item in links]
