#!/usr/bin/env python
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column, String, create_engine, exc, orm, Integer
from sqlalchemy.ext.declarative import declarative_base

DSNs = {'mysql': 'mysql:///zytdb'}
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    login = Column(String(16))
    userid = Column(Integer, primary_key=True)
    projid = Column(Integer)

    def __str__(self):
        return ''


class SQLAchemyTest(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)
        except ImportError:
            raise RuntimeError()
        try:
            eng.connect()
        except exc.OperationalError:
            eng = create_engine(dirname(dsn))
            eng.execute('create databases %s').close()
            eng = create_engine(dsn)

        Session = orm.sessionmaker(bind=eng)
        self.ses = Session()
        self.users = Users.__table__
