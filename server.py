# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/9/13 15:44
@summary:
"""
import logging
import signal
import sys

import tornado.web
from tornado import httpserver
from tornado.options import options, define
import asyncio
from core.log import configure_logging
from core.http import BaseHandler

define("port", default=8080, help="run on the given port", type=int)


class MainHandler(BaseHandler):
    def get(self):
        self.write(self.success_ret(msg='Hello World {}'.format(self.request.user_id)))


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/fy/test", MainHandler)
        ]

        super(Application, self).__init__(handlers)


def stop_callback(signum, frame):
    logging.info("%s received signum %d, process stopping", options.port, signum)
    asyncio.get_event_loop().stop()
    logging.info("%s tornado stopped", options.port)
    sys.exit(0)


def trace_callback(signum, frame):
    logging.warning("%s received signum %d, process ioloop trace", options.port, signum)
    alltasks = asyncio.Task.all_tasks()
    pending_tasks = [t for t in alltasks if not t.done()]
    pending_count = len(pending_tasks)
    logging.warning("ioloop pending count:{}".format(pending_count))
    print_tasks = pending_tasks[:5]
    for t in print_tasks:
        logging.warning("ioloop pending task:{}".format(repr(t)))


if __name__ == "__main__":
    configure_logging()
    options.parse_command_line()
    logging.info("feiyan-web runing at port %d", options.port)
    signal.signal(signal.SIGTERM, stop_callback)
    signal.signal(signal.SIGUSR2, trace_callback)

    loop = asyncio.get_event_loop()
    app = Application()
    server = httpserver.HTTPServer(app)
    server.listen(options.port)
    loop.run_forever()