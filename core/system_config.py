import os
import configparser

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_dir)
config_parser = configparser.ConfigParser()
config_file = os.path.join(project_dir, 'system.conf')
config_parser.read(config_file)

def get_mysql_server_host():
    return config_parser.get("mysql", "host")


def get_mysql_server_user():
    return config_parser.get("mysql", "user")


def get_mysql_passwd():
    return config_parser.get("mysql", "passwd")




OSS_ACCESS_KEY_ID = config_parser.get("oss", "AccessKeyId")
OSS_ACCESS_KEY_SECRET = config_parser.get("oss", "AccessKeySecret")
OSS_ENDPOINT = config_parser.get("oss", "endpoint")
OSS_BUCKET_NAME = config_parser.get("oss", "bucket")
