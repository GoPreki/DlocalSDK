import requests

from dlocal.models.card import CardPayer, CreditCard
from dlocal.models.country import Country
from dlocal.utils.requests import check_for_errors, form_headers, BASE_URL

CARDS_URL = f'{BASE_URL}/secure_cards'


def save_card_with_token(country: Country, payer: CardPayer, card_token: str) -> CreditCard:
    body = {
        'country': country.code,
        'payer': payer.to_dict(),
        'card': {
            'token': card_token
        },
    }
    req = requests.post(CARDS_URL, headers=form_headers(body=body), json=body)
    res = req.json()

    check_for_errors(req=req, res=res)

    return CreditCard.from_dict(res)


def delete_card(card_id: str):
    req = requests.delete(
        f'{CARDS_URL}/{card_id}',
        headers=form_headers(),
    )
    res = req.json()

    check_for_errors(req=req, res=res)
