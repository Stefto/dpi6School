from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker
from handler.Base import Base

class HDD(Base):
    __tablename__ = 'HDDS'

    id = Column(Integer, PRimary_key = True)
    ItemID = Column(INTEGER,nullable=False)
    price = Column(float, nullable=False)
    brand = Column(String(50), nullable=False)
    name = Column(String(150), nullable=False)
    size = Column(String(20),nllable=False)
    Shop = Column(String(50), nullable=False)

    def __init__(self, itemID, price, brand, name, size, shop):
        self.ItemID = itemID
        self.price = price
        self.brand = brand
        self.name = name
        self.size = size
        self.shop = shop

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}