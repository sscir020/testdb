# from sqlalchemy import Column,String,Integer
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
# class Item(Base):
#     __tablename__='items'
#     item_id=Column(Integer,nullable=False,primary_key=True)
#     item_name=Column(String(32),nullable=False,unique=True,index=True)
#     num=Column(Integer,nullable=False,default=0)
#     comment=Column(String(20),nullable=True,default='')