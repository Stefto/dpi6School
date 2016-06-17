from facade import facade
from EntityHdd import HDD

fac = facade()
for x in fac.getHDDByItemID(1):
    print(x.name)

for x in fac.getAllHDDs():
    print(x.name + " id= " + str(x.ItemID))