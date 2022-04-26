from dlocal.utils import requests
from dlocal.models.country import Country


def get_payment_methods(country: Country):
    return requests.get('/payments-methods', query_params={'country': country.code})
