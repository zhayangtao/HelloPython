__author__ = 'Jovi zha'
# 创建连接池
import asyncio, logging
import aiomysql
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(

    )