from typing import Optional, Union
from dlocal.models.bank_transfer import BankTransfer
from dlocal.models.country import Country
from dlocal.models.payer import Payer
from dlocal.models.payment import PaymentMethodFlow
from dlocal.payments import create_payment


def create_bank_payment(
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
) -> BankTransfer:
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

    return BankTransfer.from_dict(payment)
