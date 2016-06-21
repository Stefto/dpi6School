from facade import facade
from EntityHdd import HDD
import json

fac = facade()
h = fac.getHDDByName('WD3200LPVX')[0]

for x in fac.getHDDByItemID(h.ItemID):
    print(x.id, x.name + ' price: ' + x.price)

for x in fac.getAllHDDs():
    print(x.name + " id= " + str(x.ItemID))


#passive_dict = {}
#for i, e in enumerate(fac.getAllHDDs()):
#    passive_dict[i] = e.as_dict()
#print(json.dumps(passive_dict))