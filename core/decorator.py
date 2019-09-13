import time
import asyncio
import logging
import traceback
from functools import wraps


def print_func_spent_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        result = func(*args, **kwargs)
        dur = time.time() - start_ts
        logging.info('{} {} took {:.2} seconds'.format(func.__name__, (args, kwargs), dur))
        return result

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_ts = time.time()
        result = await func(*args, **kwargs)
        dur = time.time() - start_ts
        logging.info('{} {} took {:.2} seconds'.format(func.__name__, (args, kwargs), dur))
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return wrapper


def catch_exception(func):
    """捕获异常，并将错误信息打印到日志"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            logging.error(traceback.format_exc())

    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except:
            logging.error(traceback.format_exc())

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return wrapper
