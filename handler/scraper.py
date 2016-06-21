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
    break;
    currentLink=href.attrib['href']
    if (currentLink!=previousLink):
        previousLink=currentLink
        tmp = requests.get('https://www.4launch.nl'+ currentLink)

        table = html.fromstring(tmp.content).xpath('//tr')
        name= table[7].xpath('//td')[9].text.strip()

        if (fac.getHDDByName(name).count(name)>= 1 ):
            break
        brand = currentLink.split('-')[1]
        tmp =table[7].xpath('//td')[15].text.replace('\u20ac', '').replace(',', '.')[1:]#.encode('utf-8')[4:]
        price = float(tmp)
        size = table[7].xpath('//td')[25].text
        nextItem =fac.getnextItemid()
        if (nextItem == None):
            nextItem =1
        else:
            nextItem = nextItem.ItemID +1
        newItem = HDD(nextItem,price,brand,name,size, shop, 'https://www.4launch.nl' + currentLink)
        fac.saveHDD(newItem)

print('finished 4launch')
#afuture
r = requests.get('https://www.afuture.nl/productlist.php?categoryID=219&pag=1&sort=2&icFeatureID1926[]=2.5&queryfield=')
tree = html.fromstring(r.content)
trs = tree.xpath('//td[@class="td-description"]/a')

shop = 'https://www.afuture.nl'
for href in trs:
    currentLink=href.attrib['href']
    if (currentLink!=previousLink):
        previousLink=currentLink
        tmp = requests.get(shop + currentLink)
        table = html.fromstring(tmp.content)

        name =table.xpath('//meta[@itemprop="sku"]')[0].attrib['content'].strip()

        brand = table.xpath('//meta[@itemprop="brand"]')[0].attrib['content']
        price2 = table.xpath('//meta[@itemprop="price"]')[0].attrib['content']
        price = float(price2.replace(',', '.') + '0')
        try:
            size = tmp.content.decode('utf8').split('<th>Opslagcapaciteit harde schijf</th>')[1].split('<td>')[1].split('</td>')[0].strip()
        except IndexError:
            size = 'unknown'

        if (fac.getHDDByName(name).count(name)>= 1 ):
            nextItem =fac.getHDDByName(name)[0].ItemID
        else:
            nextItem =fac.getnextItemid()
            if (nextItem == None):
                nextItem =1
            else:
                nextItem = nextItem.ItemID +1
        newItem = HDD(nextItem,price,brand,name,size, shop, shop + currentLink)
        fac.saveHDD(newItem)

r = requests.get('https://www.afuture.nl/productlist.php?categoryID=219&pag=2&sort=2&icFeatureID1926[]=2.5&queryfield=')
tree = html.fromstring(r.content)
trs = tree.xpath('//td[@class="td-description"]/a')

for href in trs:
    currentLink=href.attrib['href']
    if (currentLink!=previousLink):
        previousLink=currentLink
        tmp = requests.get(shop + currentLink)
        table = html.fromstring(tmp.content)

        name =table.xpath('//meta[@itemprop="sku"]')[0].attrib['content'].strip()

        brand = table.xpath('//meta[@itemprop="brand"]')[0].attrib['content']
        price2 = table.xpath('//meta[@itemprop="price"]')[0].attrib['content']
        price = float(price2.replace(',', '.') + '0')
        try:
            size = tmp.content.decode('utf8').split('<th>Opslagcapaciteit harde schijf</th>')[1].split('<td>')[1].split('</td>')[0].strip()
        except IndexError:
            size = 'unknown'

        if (fac.getHDDByName(name).count(name)>= 1 ):
            nextItem =fac.getHDDByName(name)[0].ItemID
        else:
            nextItem =fac.getnextItemid()
            if (nextItem == None):
                nextItem =1
            else:
                nextItem = nextItem.ItemID +1
        newItem = HDD(nextItem,price,brand,name,size, shop, shop + currentLink)
        fac.saveHDD(newItem)

print('done')

#cool blue
#r = requests.get('http://www.hardeschijfstore.nl/category/183881/interne-harde-schijven.html?9218=24275&items=48')
#tree = html.fromstring(r.content)
#trs = tree.xpath('//div[@class="product-item--block product-item--block-details"]')

#eigenaardigheidje van cool blue...
#shop = 'http://http://www.hardeschijfstore.nl'
#print(trs)
#for href in trs:
    #currentLink=href.attrib['href']
    #if (currentLink!=previousLink):
        #print(shop + currentLink)


#paradigit
#r = requests.get('https://www.paradigit.nl/opslag/interne-harde-schijven/')
#tree = html.fromstring(r.content)
#trs = tree.xpath('//div[@class="col-sm-7 productitem-container"]/h2/a')

#shop = 'https://www.Paradigit.nl'
#for href in trs:
    #currentLink=href.attrib['href']
    #if (currentLink!=previousLink):
        #tmp = requests.get(shop + currentLink, verify=False)
        #print(tmp)
        #table = html.fromstring(tmp.content).xpath('//div[class="readmore_collapse"]')
        #print(table)
        #for t in table:
        #    print(t)