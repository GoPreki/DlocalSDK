import requests

from typing import Optional, Union
from dlocal.models.country import Country
from dlocal.models.payer import Payer
from dlocal.models.payment import CardPayment, PaymentMethodFlow
from dlocal.models.card import CardPayer, CreditCard, PaymentCreditCard
from dlocal.payments import create_payment
from dlocal.utils.exceptions import DlocalErrorCode, DlocalException
from dlocal.utils.requests import check_for_errors, form_headers, BASE_URL

CARDS_URL = f'{BASE_URL}/secure_cards'


def create_card_payment(
    amount: Union[int, float],
    currency: str,
    country: Country,
    payer: Payer,
    credit_card: PaymentCreditCard,
    order_id: str,
    original_order_id: Optional[str] = None,
    description: Optional[str] = None,
    notification_url: Optional[str] = None,
    callback_url: Optional[str] = None,
) -> CardPayment:
    if not credit_card.card_id and not credit_card.token:
        raise DlocalException(code=DlocalErrorCode.MISSING_INPUTS.value,
                              message='Missing mandatory inputs for payment creation')

    payment = create_payment(
        amount=amount,
        currency=currency,
        payment_method_flow=PaymentMethodFlow.DIRECT,
        country=country,
        payer=payer,
        card=credit_card,
        order_id=order_id,
        payment_method_id='CARD',
        original_order_id=original_order_id,
        description=description,
        notification_url=notification_url,
        callback_url=callback_url,
    )

    return CardPayment.from_dict(payment)


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
