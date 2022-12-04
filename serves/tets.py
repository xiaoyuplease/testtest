import os
import yaml
from arize_auto_test.logger import logger

basePath = os.path.dirname(os.path.dirname(__file__))


def open_yaml_page(file):
    with open(basePath + "/page/%s" % file + ".yaml", "r", encoding="utf-8") as f:
        f = yaml.load(f, Loader=yaml.FullLoader)
    logger.debug(f)
    return f


open_yaml_page("access_page")
