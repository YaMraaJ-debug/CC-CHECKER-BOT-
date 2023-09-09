import json
import sys
from redis import Redis as r
import aioredis as redis
from jocasta.utlis.logger import log
from jocasta.config import get_int_key, get_str_key
import asyncio


aiopool = redis.ConnectionPool(
    host = get_str_key("REDIS_URI",1),
    port = get_int_key("REDIS_PORT",1),
    # db= get_str_key("REDIS_DB_NAME", 1),
    # password= get_str_key("REDIS_PASS", 1),
    decode_responses= True,
    socket_connect_timeout = 20,
    socket_timeout = 20,
)

aioredis = redis.Redis(
    connection_pool= aiopool
    # host = get_str_key("REDIS_URI",1),
    # port = get_int_key("REDIS_PORT",1),
    # # db= get_str_key("REDIS_DB_NAME", 1),
    # password= get_str_key("REDIS_PASS", 1),
    # decode_responses= True,
    # socket_connect_timeout = 10,
    # socket_timeout = 10,
)


try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(aioredis.ping())
    log.info("REDIS STARTED..")
except Exception as e:
    log.warn("Error while connecting to redis. Error: {}".format(e))
    sys.exit(2)