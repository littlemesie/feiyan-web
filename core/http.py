import json
import time
import logging

import aiohttp
import tornado
from tornado import web

aiohttp_client = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60))


class BaseHandler(tornado.web.RequestHandler):

    def options(self):
        self.set_status(204)
        self.finish()

    def prepare(self):
        # logging.info('request headers: %s', self.request.headers)
        self.request.user_id = self.request.headers.get('User_id', None)

    @staticmethod
    def success_ret(msg="", code="", data=None):
        t = int(time.time() * 1000)
        ret = {"success": True, "sys_time": t, "code": code, "msg": msg}
        if data is not None:
            ret["data"] = data
        return json.dumps(ret)

    @staticmethod
    def error_ret(msg="", code="", data=None):
        t = int(time.time() * 1000)
        ret = {"success": False, "sys_time": t, "code": code, "msg": msg}
        if data is not None:
            ret["data"] = data
        return json.dumps(ret)
