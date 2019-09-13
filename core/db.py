import logging
import asyncio
from core.pool_wrapper import PoolWrapper
from core.mysql_conn import MysqlConn

from core.constants import DB_DEFAULT_MINCACHED, DB_DEFAULT_MAXCACHED, DB_DEFAULT_MINSIZE, DB_DEFAULT_MAXSIZE, \
    DB_DEFAULT_POOL_RECYCLE, DB_DEFAULT_PORT, DB_NAME
from core import system_config

loop = asyncio.get_event_loop()


class Base_MysqlConn(MysqlConn):
    pool = PoolWrapper(mincached=DB_DEFAULT_MINCACHED,
                       maxcached=DB_DEFAULT_MAXCACHED,
                       minsize=DB_DEFAULT_MINSIZE,
                       maxsize=DB_DEFAULT_MAXSIZE,
                       loop=loop,
                       echo=False,
                       pool_recycle=DB_DEFAULT_POOL_RECYCLE,
                       host=system_config.get_mysql_server_host(),
                       user=system_config.get_mysql_server_user(),
                       password=system_config.get_mysql_passwd(),
                       db=DB_NAME,
                       port=DB_DEFAULT_PORT,
                       )

    """docstring for Base_MysqlConn"""

    def __init__(self):
        super(Base_MysqlConn, self).__init__()


