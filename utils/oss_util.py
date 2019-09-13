# -*- coding:utf-8 -*-

"""
@ide: PyCharm
@author: mesie
@date: 2019/9/13 16:25
@summary:
"""
import oss2
from core.system_config import OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_ENDPOINT, OSS_BUCKET_NAME

auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)


def get_oss_url(key):
    """从 oss key 获取文件访问地址"""
    bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)
    pic_url = bucket.sign_url('GET', key, 600)
    return pic_url


def upload_file_to_oss(key, data, content_type):
    """
    保存文件到oss
    :param key: oss key
    :param data: bytes，str或file-like object
    """
    oss_bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)
    oss_bucket.put_object(key, data, headers={'Content-Type': content_type})