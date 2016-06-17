from EntityHdd import HDD
from Base import Base
from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

class facade:

    def __init__(self):
        engine = create_engine('sqlite:///dpi.db')
        Base.metadata.bind =engine
        DBSession = sessionmaker(bind=engine)
        self.Session = DBSession()

        metadata = MetaData(engine)
        Table('HDDS', metadata,
        Column('id',Integer, primary_key = True),
        Column('ItemID',INTEGER,nullable=False),
        Column('price',String(10), nullable=False),
        Column('brand',String(50), nullable=False),
        Column('name',String(150), nullable=False),
        Column('size',String(20),nullable=False),
        Column('Shop',String(50), nullable=True),
        Column('url',String(255), nullable=True)).create(checkfirst=True)

        metadata.create_all()

    def getHDD(self,id):
        return self.Session.query(HDD).filter_by(id = id).first()

    def getAllHDDs(self):
        return self.Session.query(HDD).all()

    def getHDDByItemID(self,ItemID):
        return self.Session.query(HDD).filter_by(ItemID=ItemID).all()

    def getHDDByName(self,name):
        return self.Session.query(HDD).filter_by(name=name).all()

    def saveHDD(self,HDD):
        self.Session.add(HDD)
        self.Session.commit()

    def getnextItemid(self):
        return self.Session.query(HDD).order_by(HDD.ItemID.desc()).first()

    def getHDDByPrice(self,order):
        if (order == 'desc'):
            return self.Session.query(HDD).order_by(HDD.price.desc()).all()
        else:
            return self.Session.query(HDD).order_by(HDD.price.asc()).all()