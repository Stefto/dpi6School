from facade import facade
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

for href in trs:
    currentLink=href.attrib['href']
    if (currentLink==previousLink):
        break
    else:
        previousLink=currentLink
        tmp = requests.get('https://www.4launch.nl'+ currentLink)

        table = html.fromstring(tmp.content).xpath('//tr')
        name= table[7].xpath('//td')[7].text

        if (fac.getHDDByName(name)== 1 ):
            break
        brand = currentLink.split('-')[1]
        price = table[7].xpath('//td')[15].text.encode('utf-8')[4:]
        size = table[7].xpath('//td')[25].text
        print(price)
        print(name)
        print(brand)
        print(size)
        newItem = HDD(fac.getnextItemid +1,price,brand,name,size,'www.4launch.nl','https://www.4launch.nl'+ currentLink)
        fac.saveHDD(newItem)
        break;