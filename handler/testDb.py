from facade import facade
from EntityHdd import HDD
import json

fac = facade()
for x in fac.getHDDByItemID(1):
    print(x.name)

for x in fac.getAllHDDs():
    print(x.name + " id= " + str(x.ItemID))


passive_dict = {}
for i, e in enumerate(fac.getAllHDDs()):
    passive_dict[i] = e.as_dict()
print(json.dumps(passive_dict))