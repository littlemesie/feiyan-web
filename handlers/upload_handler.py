# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/11/3 10:30
@summary:
"""
import time
import logging
from utils import oss_util
from core.decorator import catch_exception
from core.http import BaseHandler

class UploadHandler(BaseHandler):
    """上传文件"""

    def get(self):
        self.render("../templates/upload.html", error=None)

    @catch_exception
    async def post(self):
        file = self.request.files["file"][0]["body"]
        cur_time = int(time.time() * 1000)
        file_name = str(cur_time) + '.png'
        oss_util.upload_file_to_oss(file_name, file, 'png')
        self.write(BaseHandler.success_ret(code=200, msg='ok'))