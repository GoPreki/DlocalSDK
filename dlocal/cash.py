import requests

from typing import Optional, Union
from dlocal.models.country import Country
from dlocal.models.payer import Payer
from dlocal.models.payment import CashPayment, PaymentMethodFlow
from dlocal.payments import PAYMENTS_URL, create_payment
from dlocal.utils.requests import check_for_errors, form_headers


def create_cash_payment(
    amount: Union[int, float],
    currency: str,
    country: Country,
    payer: Payer,
    order_id: str,
    payment_method_id: str,
    original_order_id: Optional[str] = None,
    description: Optional[str] = None,
    notification_url: Optional[str] = None,
    callback_url: Optional[str] = None,
) -> CashPayment:
    payment = create_payment(
        amount=amount,
        currency=currency,
        payment_method_flow=PaymentMethodFlow.DIRECT,
        country=country,
        payer=payer,
        order_id=order_id,
        payment_method_id=payment_method_id,
        original_order_id=original_order_id,
        description=description,
        notification_url=notification_url,
        callback_url=callback_url,
    )

    return CashPayment.from_dict(payment)


def cancel_payment(id: str) -> CashPayment:
    req = requests.post(f'{PAYMENTS_URL}/{id}/cancel', headers=form_headers())
    res = req.json()
    print(f'{PAYMENTS_URL}/{id}/cancel')
    check_for_errors(req=req, res=res)

    return CashPayment.from_dict(res)
