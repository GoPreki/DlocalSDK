import requests

from dlocal.models.country import Country
from dlocal.utils.requests import check_for_errors, form_headers, BASE_URL


def get_payment_methods(country: Country):
    req = requests.get(f'{BASE_URL}/payments-methods', headers=form_headers(), params={'country': country.code})
    res = req.json()

    check_for_errors(req=req, res=res)

    return res
