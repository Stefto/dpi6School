from handler.EntityHdd import HDD
from handler.Base import Base
from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

class facade:
    Session = sessionmaker

    def __init__(self):
        engine = create_engine('mysql://root@localhost/dpi')
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine)

    def getHDD(self,id):
        return self.Session.query(HDD).filterBy(id = id).first()

    def getAllHDDs(self):
        return self.Session.query(HDD).all()

    def getHDDByItemID(self,ItemID):
        return self.Session.query(HDD).filterBy(itemID=ItemID).all()

    def getHDDByPrice(self,order):
        if (order == 'desc'):
            return self.Session.query(HDD).order_by(HDD.price.desc()).all()
        else:
            return self.Session.query(HDD).order_by(HDD.price.asc()).all()