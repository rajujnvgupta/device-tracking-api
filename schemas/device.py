# schemaa helps to serialize and also convert mangodb format json to our UI needed

        # "id":   str(db_item["_id"]),

def deviceEntity(db_item) -> dict:
    return {
        "device_fk_id": db_item["device_fk_id"],
        "latitude": db_item["latitude"],
        "longitude": db_item["longitude"],
        "time_stamp": db_item["time_stamp"],
        "sts"       : db_item["sts"],
        "speed"     : db_item["speed"]
    }

def listOfDeviceEntity(db_item_list) -> list:
    list_device_entity = []
    for item in db_item_list:
        list_device_entity.append(deviceEntity(item))

    return list_device_entity



    # device_fk_id :  str
    # latitude :  str
    # longitude:  str
    # timme_stamp: datetime
    # sts        : datetime
    # speed      : int