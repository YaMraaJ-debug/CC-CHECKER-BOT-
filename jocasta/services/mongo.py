import sys
from jocasta.utlis.logger import log
from jocasta.config import get_str_key, get_int_key
import asyncio
import motor.motor_asyncio
from pymongo import MongoClient
import asyncio

database_name = name if (name:= get_str_key("MONGO_DB",1)) else "bot"
# mongo = MongoClient(
#     get_str_key('MONGO_URL',1)
# )
async_client = motor.motor_asyncio.AsyncIOMotorClient(get_str_key('MONGO_URL',1), serverSelectionTimeoutMS=5000)


try:
    # db = mongo[database_name]
    adb = async_client[database_name]
    log.info("MONGO DATABASE STARTED...")
except:
    log.warn("Error While Connecting To Mongo")
    sys.exit(2)
