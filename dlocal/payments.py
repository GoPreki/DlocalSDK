from typing import Optional, Union
from dlocal.models.card import PaymentCreditCard
from dlocal.models.country import Country
from dlocal.models.payer import Payer
from dlocal.models.payment import PaymentMethodFlow, RedirectPayment
from dlocal.utils import optional_dict
from dlocal.utils.exceptions import DlocalErrorCode, DlocalException
from dlocal.utils.requests import post

PAYMENTS_PATH = '/payments'
SECURE_PAYMENTS_PATH = '/secure_payments'


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

    return post(path=SECURE_PAYMENTS_PATH if use_secure_url else PAYMENTS_PATH, body=body)


def create_redirect_payment(
    amount: Union[int, float],
    currency: str,
    country: Country,
    payer: Payer,
    order_id: str,
    callback_url: str,
    payment_method_id: str,
    original_order_id: Optional[str] = None,
    description: Optional[str] = None,
    notification_url: Optional[str] = None,
) -> RedirectPayment:
    if not callback_url:
        raise DlocalException(code=DlocalErrorCode.MISSING_INPUTS.value,
                              message='Missing mandatory inputs for payment creation')

    payment = create_payment(
        amount=amount,
        currency=currency,
        payment_method_flow=PaymentMethodFlow.REDIRECT,
        country=country,
        payer=payer,
        order_id=order_id,
        payment_method_id=payment_method_id,
        original_order_id=original_order_id,
        description=description,
        notification_url=notification_url,
        callback_url=callback_url,
    )

    return RedirectPayment.from_dict(payment)
