import os
import logging.config

from core.system_config import project_dir


def configure_logging(path=None, logging_settings=None):
    if logging_settings is None:
        if path:
            root_log_file = os.path.join(project_dir, 'log/{}/root.log'.format(path))
            debug_log_file = os.path.join(project_dir, 'log/{}/debug.log'.format(path))
            root_json_log_file = os.path.join(project_dir, 'log/{}/root_json.log'.format(path))
        else:
            root_log_file = os.path.join(project_dir, 'log/root.log')
            debug_log_file = os.path.join(project_dir, 'log/debug.log')
            root_json_log_file = os.path.join(project_dir, 'log/root_json.log')
        logging_settings = {
            'version': 1,
            'formatters': {
                'simple': {
                    'format': '{message}',
                    'style': '{',
                },
                'normal': {
                    'format': '{asctime} {levelname} {pathname} {lineno} {process:d} {thread:d} {message}',
                    'style': '{',
                },
                "json": {
                    "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    'format': '%(asctime) %(levelname) %(module) %(filename) %(pathname) %(lineno) %(process) %(thread) %(message)',
                }
            },
            'handlers': {
                'debug': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'maxBytes': 2097152,
                    'backupCount': 1,
                    'filename': debug_log_file,
                    'formatter': 'normal'
                },
                'root': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'maxBytes': 1024000000,
                    'backupCount': 10,
                    'filename': root_log_file,
                    'formatter': 'normal'
                },
                'root_json': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'maxBytes': 1024000000,
                    'backupCount': 1,
                    'filename': root_json_log_file,
                    'formatter': 'json'
                },

            },
            'loggers': {
                '': {
                    'handlers': ['debug', 'root', 'root_json'],
                    'level': 'DEBUG',
                    'propagate': False,
                }
            },
        }
    logging.config.dictConfig(logging_settings)
