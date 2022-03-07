import os
import json
import hashlib
import hmac

from dlocal.utils.dates import now_in_isoformat
from dlocal.utils.exceptions import DlocalException

_prefix = 'api' if not os.environ.get('DLOCAL_TEST', True) else 'sandbox'
BASE_URL = f'https://{_prefix}.dlocal.com'

X_LOGIN = os.environ['DLOCAL_X_LOGIN']
X_TRANS_KEY = os.environ['DLOCAL_X_TRANS_KEY']


def form_headers(body=None) -> dict:
    x_date = now_in_isoformat()
    return {
        'X-Date': x_date,
        'X-Login': X_LOGIN,
        'X-Trans-Key': X_TRANS_KEY,
        'Content-Type': 'application/json',
        'X-Version': '2.1',
        'User-Agent': 'Preki API',
        'Authorization': f'V2-HMAC-SHA256, Signature: {generate_signature(x_date, body)}',
    }


def generate_signature(date, body):
    body_str = json.dumps(body) if body else ''

    return hmac.new(
        os.environ['DLOCAL_SECRET_KEY'].encode('utf8'),
        (X_LOGIN + date + body_str).encode('utf8'),
        hashlib.sha256,
    ).hexdigest()


def check_for_errors(req, res):
    if req.status_code >= 400:
        raise DlocalException(code=res.get('code'),
                              param=res.get('param'),
                              message=res.get('message', f'Unkwnon Dlocal error occured: {str(res)}'))
