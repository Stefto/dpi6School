from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker
from Base import Base

class HDD(Base):
    __tablename__ = 'HDDS'

    id = Column(Integer, primary_key = True)
    ItemID = Column(INTEGER,nullable=False)
    price = Column(REAL(), nullable=False)
    brand = Column(String(50), nullable=False)
    name = Column(String(150), nullable=False)
    size = Column(String(20), nullable=False)
    Shop = Column(String(50), nullable=True)
    url = Column(String(255), nullable=True)

    def __init__(self, itemID, price, brand, name, size, shop,url):
        self.ItemID = itemID
        self.price = price
        self.brand = brand
        self.name = name
        self.size = size
        self.shop = shop
        self.url = url

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}