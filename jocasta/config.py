# from config import Config
import os
import yaml
from jocasta.utlis.logger import log
from envparse import env

ALL_USER_DATA = {
    "REDIS_PORT": 6379,
    "REDIS_URL": "localhost",
}


if os.name == "nt":
    CONFIG_PATH = os.getcwd() + '\\jocasta\\configs\\bot_conf.yaml'
    log.info("Using Windows Config Path.")
else:
    CONFIG_PATH = os.getcwd() + '/jocasta/configs/bot_conf.yaml'
    log.info("Using Linux Config Path.")


if os.path.isfile(CONFIG_PATH):
    for item in (data := yaml.load(open(CONFIG_PATH, 'r'), Loader = yaml.FullLoader)):
        ALL_USER_DATA[item.upper()] = data[item]
    log.info("Added all config..")


def get_bool_key(name, req = False):
    DEFAULT = ALL_USER_DATA[name] if name in ALL_USER_DATA else None
    if not (data := env.bool(name, default = DEFAULT)) and not req:
        log.warn("%s not found"% name)
        return None
    elif not data and req:
        log.warn("%s not found"% name)
        exit()
    else:
        return data


def get_str_key(name, req = False):
    """Get string if name found else exit 

    params:
        name (str): name you want to get
        req (bool, optional): true if requires. Defaults to False.

    Returns:
        [None, data]: [return None if req is False else data]
    """
    DEFAULT = ALL_USER_DATA[name] if name in ALL_USER_DATA else None
    if not (data := env.str(name, default = DEFAULT)) and not req:
        log.warn("%s not found"% name)
        return None
    elif not data and req:
        log.warn("%s not found"% name)
        exit()
    else:
        return data

def get_int_key(name, req = False):
    """Get intger if name found else exit 

    params:
        name (int): name you want to get
        req (bool, optional): true if requires. Defaults to False.

    Returns:
        [None, data]: [return None if req is False else data]
    """
    DEFAULT = ALL_USER_DATA[name] if name in ALL_USER_DATA else None
    if not (data := env.int(name, default = DEFAULT)) and not req:
        log.warn("%s not found"% name)
        return None
    elif not data and not req:
        log.warn("%s not found"% name)
        exit()
    else:
        return data


def get_list_key(name, req = False):
    DEFAULT = ALL_USER_DATA[name] if name in ALL_USER_DATA else None
    if not (data := env.list(name, default = DEFAULT)) and not req:
        log.warn("%s not found"% name)
        return None
    elif not data and not req:
        log.warn("%s not found"% name)
        exit()
    else:
        return data



