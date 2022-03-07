import requests

from typing import Optional, Union
from dlocal.models.card import PaymentCreditCard
from dlocal.models.country import Country
from dlocal.models.payer import Payer
from dlocal.models.payment import PaymentMethodFlow
from dlocal.utils import optional_dict
from dlocal.utils.requests import check_for_errors, form_headers, BASE_URL

PAYMENTS_URL = f'{BASE_URL}/payments'
SECURE_PAYMENTS_URL = f'{BASE_URL}/secure_payments'


def create_payment(
    amount: Union[int, float],
    currency: str,
    payment_method_flow: PaymentMethodFlow,
    country: Country,
    payer: Payer,
    order_id: str,
    payment_method_id: Optional[str] = None,
    original_order_id: Optional[str] = None,
    description: Optional[str] = None,
    notification_url: Optional[str] = None,
    callback_url: Optional[str] = None,
    use_secure_url: bool = False,  # Only needed for payments made with credit card information
    card: Optional[PaymentCreditCard] = None,
):
    optional_data = optional_dict(
        payment_method_id=payment_method_id,
        original_order_id=original_order_id,
        description=description,
        notification_url=notification_url,
        callback_url=callback_url,
        card=card.to_dict() if card else None,
    )
    body = {
        'amount': amount,
        'currency': currency,
        'payment_method_flow': payment_method_flow.value,
        'country': country.code,
        'payer': payer.to_dict(),
        'order_id': order_id,
        **optional_data,
    }

    req = requests.post(SECURE_PAYMENTS_URL if use_secure_url else PAYMENTS_URL,
                        headers=form_headers(body=body),
                        json=body)
    res = req.json()

    check_for_errors(req=req, res=res)

    return res
