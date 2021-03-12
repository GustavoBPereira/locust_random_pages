from bs4 import BeautifulSoup
import re


def get_links(content):
    bs = BeautifulSoup(content, 'html.parser')
    links = set()
    for link in bs.find_all('a', href=re.compile('^(/)')):
        if 'href' in link.attrs:
            links.add(link.attrs['href'])
    return links
