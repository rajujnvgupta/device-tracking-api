from fastapi import APIRouter
from models.device import DeviceInfo
from config.database import connection
from schemas.device import deviceEntity, listOfDeviceEntity
from config.redis_cache import BaseCache
from config import settings
import traceback
import time
import json
import pickle
import re
from dateutil import parser
from datetime import datetime


from bson import ObjectId

device_router = APIRouter()

redis_conn = None

def redis_connection():
    redis_conn = BaseCache(**settings.REDIS_CACHE_DB)

def json_serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return obj.isoformat()


@device_router.get('/hello')
async def hello_world():
    return "hellow world"
redis_conn = None

@device_router.get('/device_curr_info/{device_fk_id}')
async def find_device_curr_info_by_id(device_fk_id):

    '''getting latest info for {device_fk_id} from redis if not in redis then read from database and set into redis'''

    global redis_conn
    if not redis_conn:
        redis_conn = redis_conn = BaseCache(**settings.REDIS_CACHE_DB)
    data = redis_conn.get(device_fk_id)
    if data:
        print("device info found in redis")
        data = data.decode('utf8')
        return json.loads(data)
    else:
        data = listOfDeviceEntity(connection.local.DeviceInfo.find({"device_fk_id": int(device_fk_id)}).sort("time_stamp", -1).limit(1))[0]
        if data:
            print("device info fetched from database")
            redis_conn.set(device_fk_id, json.dumps(data , default=json_serialize).encode('utf-8'))
            return data
    dict_data = deviceEntity(connection.local.DeviceInfo.find_one({"device_fk_id": int(device_fk_id)}))
    return dict_data


@device_router.get('/device_location_curr/{device_fk_id}')
async def find_device_info(device_fk_id):
    ''' getting latest device location with device_fk_id. It read data from redis for specified {device_fk_id} and return from there itself if present otherwise go to db '''

    global redis_conn
    if not redis_conn:
        redis_conn = redis_conn = BaseCache(**settings.REDIS_CACHE_DB)
        # redis_conn = redis_connection()
    device_fk_id_key = device_fk_id + "_key"
    data = redis_conn.get(device_fk_id_key)
    if data:
        data = data.decode('utf-8')
        return json.loads(data)
    else:
        data = listOfDeviceEntity(connection.local.DeviceInfo.find({"device_fk_id": int(device_fk_id)}).sort("time_stamp", -1).limit(1))[0]
        location_info = {"latitude" : data["latitude"], "longitude" : data["longitude"]}
        if data:
            print("device location fetched from databse")
            redis_conn.set(device_fk_id_key, json.dumps(location_info).encode('utf-8'))

        return location_info

#getting device location between start_time and end_time
@device_router.get('/track_device_location/{device_fk_id}/{start_time}/{end_time}')
async def find_track_device_location(device_fk_id, start_time, end_time):

    '''tracking device location using {time_stamp} between start_time and end_time for particular device id'''
    start_time = parser.isoparse(start_time)
    end_time = parser.isoparse(end_time)
    return listOfDeviceEntity(connection.local.DeviceInfo.find({"time_stamp": {'$gte': start_time, '$lt': end_time}}))

