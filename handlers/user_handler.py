# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/9/13 16:34
@summary:
"""
import time
import traceback
import logging
from core import system_config
from core import db
from core.decorator import catch_exception
from core.http import BaseHandler

class UserHandler(BaseHandler):
    """提交"""

    @catch_exception
    async def post(self):
        cur_time = time.time()
        today = int(cur_time - cur_time % 86400) * 1000

        self.write(BaseHandler.success_ret(code=200, msg='ok'))