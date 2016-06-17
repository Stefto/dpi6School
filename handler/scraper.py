from facade import facade
from EntityHdd import HDD
import json
import requests
from lxml import html

fac = facade()

#4launch scraping 2.5 inch hdd
r = requests.get('https://www.4launch.nl/producten/categorie/Componenten/Harddisks/SATA---2.5-Inch/93')
tree = html.fromstring( r.content)
trs = tree.xpath('//td[@class="l"]/a')

previousLink = ''
currentLink = ''
shop ='www.4launch.nl'

for href in trs:
    currentLink=href.attrib['href']
    if (currentLink!=previousLink):
        previousLink=currentLink
        tmp = requests.get('https://www.4launch.nl'+ currentLink)

        table = html.fromstring(tmp.content).xpath('//tr')
        name= table[7].xpath('//td')[7].text

        if (fac.getHDDByName(name).count(name)>= 1 ):
            break
        brand = currentLink.split('-')[1]
        price = table[7].xpath('//td')[15].text.replace('\u20ac', ',')[2:]#.encode('utf-8')[4:]
        size = table[7].xpath('//td')[25].text
        nextItem =fac.getnextItemid()
        if (nextItem == None):
            nextItem =1
        else:
            nextItem = nextItem.ItemID +1
        newItem = HDD(nextItem,price,brand,name,size, shop, 'https://www.4launch.nl' + currentLink)
        fac.saveHDD(newItem)