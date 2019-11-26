from django.db import models


class Product(Base):
    """docstring for Products"""
    id = Column(Integer, primary_key=True)
    ean = Column(String(13), nullable=False)
    name = Column(String(50))
    category = Column(Integer, ForeignKey('category.id'))
    substitute = Column(Integer, ForeignKey('product.id'))
    substituted = Column(Boolean)


class Category(Base):
    """docstring for Categories"""
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return str((self.name))


class Favourite(object):
    """docstring for Favourite"""

    def __init__(self, arg):
        super(Favourite, self).__init__()
        self.arg = arg
