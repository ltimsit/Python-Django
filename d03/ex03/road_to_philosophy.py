import requests, sys
from bs4 import BeautifulSoup as bs

def get_to_next(page):
    print(page)
    if page == 'Philosophy':
        exit("SUCCESS !!")
    wikip = "https://en.wikipedia.org/wiki/"
    r = requests.get(wikip+page)
    soup = bs(r.text, features="html.parser")
    elem = soup.find('div', attrs={'class': u'mw-parser-output'}).findAll('p')
    # print(elem)
    for el in elem:
        links = el.findAll('a')
        for link in links:
            if not link is None:
                ref = link.attrs['href']
                # print(ref[:6])
                start = ref[:6]
                # print('apres', ref[6:])
                if start == '/wiki/':
                    if ref[6:].find(":") == -1:
                        if ref[6:] is not 'Latin':
                            get_to_next(ref[6:])
                            exit()
                        # pass
    # exit()

if __name__=='__main__':
    if len(sys.argv) != 2:
        exit()
    get_to_next(sys.argv[1])
