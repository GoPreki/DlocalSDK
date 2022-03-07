from datetime import datetime


def now_in_isoformat():
    return datetime.utcnow().isoformat()[:-3] + 'Z'


def isoformat_to_timestamp(isoformat_date, date_format='%Y-%m-%dT%H:%M:%S.%f%z'):
    return datetime.strptime(isoformat_date, date_format).timestamp()
