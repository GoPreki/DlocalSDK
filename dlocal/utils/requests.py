import json
import hashlib
import hmac
import requests

from urllib.parse import quote
from dlocal.utils.dates import now_in_isoformat
from dlocal.utils.exceptions import DlocalErrorCode, DlocalException


class Keys:
    X_LOGIN = None
    X_TRANS_KEY = None
    SECRET_KEY = None

    TEST: bool = True


_prefix = 'api' if not Keys.TEST else 'sandbox'
BASE_URL = f'https://{_prefix}.dlocal.com'


def form_headers(body=None) -> dict:
    if not Keys.X_LOGIN or not Keys.X_TRANS_KEY or not Keys.SECRET_KEY:
        raise DlocalException(code=DlocalErrorCode.MISSING_KEYS.value, message='Keys were not correctly initialized')

    x_date = now_in_isoformat()
    return {
        'X-Date': x_date,
        'X-Login': Keys.X_LOGIN,
        'X-Trans-Key': Keys.X_TRANS_KEY,
        'Content-Type': 'application/json',
        'X-Version': '2.1',
        'User-Agent': 'Preki API',
        'Authorization': f'V2-HMAC-SHA256, Signature: {generate_signature(x_date, body)}',
    }


def generate_signature(date, body):
    if not Keys.SECRET_KEY:
        raise DlocalException(code=DlocalErrorCode.MISSING_KEYS.value, message='Keys were not correctly initialized')

    body_str = json.dumps(body) if body else ''

    return hmac.new(
        Keys.SECRET_KEY.encode('utf8'),
        (Keys.X_LOGIN + date + body_str).encode('utf8'),
        hashlib.sha256,
    ).hexdigest()


def check_for_errors(req, res):
    if req.status_code >= 400:
        raise DlocalException(code=res.get('code'),
                              param=res.get('param'),
                              message=res.get('message', f'Unknown Dlocal error occured: {str(res)}'))


def post(path='', body=None):
    req = requests.post(url=f'{BASE_URL}{path}', json=body, headers=form_headers(body=body))
    res = req.json()
    check_for_errors(req, res)
    return res


def delete(path='', body=None):
    req = requests.delete(url=f'{BASE_URL}{path}', json=body, headers=form_headers(body=body))
    res = req.json()
    check_for_errors(req, res)
    return res


def get(path='', path_params={}):
    for key, value in path_params.items():
        value = quote(value)
        path = path.replace(f'/{{{key}}}', f'/{value}')

    req = requests.get(url=f'{BASE_URL}{path}', headers=form_headers())
    res = req.json()
    check_for_errors(req, res)
    return res
