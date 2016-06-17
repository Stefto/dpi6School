from sqlalchemy.ext.declarative import declarative_base
from flask.ext.jsontools import JsonSerializableBase

Base = declarative_base(cls=(JsonSerializableBase))