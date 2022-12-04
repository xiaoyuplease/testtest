from loguru import logger
# import time
import os


def my_logger():
    logger.add("日志.log", format="{time:YYYY-MM-DD at HH:mm:ss} |    {level}  |    {message} ")
    return logger


logger = my_logger()
