from pydantic import BaseModel
from datetime import datetime

class DeviceInfo(BaseModel):
    device_fk_id :  str
    latitude :  str
    longitude:  str
    time_stamp: datetime
    sts        : datetime
    speed      : int


    # device_fk_id	latitude	longitude	time_stamp	sts	speed