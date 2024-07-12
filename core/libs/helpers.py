import random
import string
from datetime import datetime
from pytz import timezone 

TIMESTAMP_WITH_TIMEZONE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'
TS_TIMEZONE_FORMAT_1 = '%a, %d %b %Y %H:%M:%S'
TS_TIMEZONE_FORMAT_2 = '%Y-%m-%d %H:%M:%S'


class GeneralObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_utc_now():
    return datetime.utcnow()
    
def utc_format(TS_TZ_FORMAT=TIMESTAMP_WITH_TIMEZONE_FORMAT):
    return datetime.now(timezone("Asia/Kolkata")).strftime(TS_TZ_FORMAT)

