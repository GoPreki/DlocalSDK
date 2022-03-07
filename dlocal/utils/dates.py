from datetime import datetime


def now_in_isoformat():
    return datetime.utcnow().isoformat()[:-3] + 'Z'


def isoformat_to_timestamp(isoformat_date):
    return datetime.fromisoformat(isoformat_date).timestamp()
