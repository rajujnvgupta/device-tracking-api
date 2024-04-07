from config.database import connection
from config.redis_cache import BaseCache
from config import database
from models.device import DeviceInfo
import traceback
import os
import csv
import time
from dateutil import parser
# device_fk_id	latitude	longitude	time_stamp	            sts	                        speed
# 25029	        27.8779583	76.06095886	 2021-10-23T14:08:02Z	2021-10-23T14:08:08.5984Z	0


adding errro to fail execution
try:
    with open('raw_data.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        # print(type(csvFile))
        header = next(csvFile)
        # print(type(header))

        for lines in csvFile:
            # print(type(lines))
            data_dict = {}
            for idx in range(len(header)):
                if header[idx] == 'device_fk_id':
                    data_dict[header[idx]] = int(lines[idx])
                elif header[idx] == 'time_stamp' or header[idx] == 'sts':
                    data_dict[header[idx]] = parser.isoparse(lines[idx])
                elif header[idx] == 'speed':
                    data_dict[header[idx]] = int(lines[idx])
                else:
                    data_dict[header[idx]] = lines[idx]

            print(data_dict)
            try:
                connection.local.DeviceInfo.insert_one(dict(data_dict))
            except:
                print("exception while inserting into db is: %s", traceback.format_exc())


except:
    print("exception while reading raw_data.csv is: %s", traceback.format_exc())
