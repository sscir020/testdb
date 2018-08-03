from app.models1 import Item
from app import dbsession
import unittest

class SqlATestCase(unittest.TestCase):
    def test_sqla(self):
        items=dbsession.query(Item).all()
        print(items)
        print(items.count(Item))
        i=0
        for item in items:
            print(item.item_name)
            i+=1
            item.comment=i
            dbsession.add(item)
        dbsession.commit()
        dbsession.close()