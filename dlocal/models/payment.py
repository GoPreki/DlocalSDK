from enum import Enum
from dataclasses import dataclass
from dlocal.models.card import CreditCard
from dlocal.utils import optional_dict
from dlocal.utils.dates import isoformat_to_timestamp


class PaymentMethodFlow(Enum):
    DIRECT = 'DIRECT'
    REDIRECT = 'REDIRECT'


class PaymentStatus(Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    REJECTED = 'REJECTED'
    CANCELLED = 'CANCELLED'
    EXPIRED = 'EXPIRED'
    AUTHORIZED = 'AUTHORIZED'
    VERIFIED = 'VERIFIED'


@dataclass
class Payment:
    id: str
    method_id: str
    method_type: str
    creation_date: float
    approval_date: float
    device_id: str
    status: PaymentStatus
    status_detail: str
    status_code: int

    def to_dict(self) -> dict:
        return optional_dict(
            id=self.id,
            method_id=self.method_id,
            method_type=self.method_type,
            created_date=self.creation_date,
            approved_date=self.approval_date,
            device_id=self.device_id,
            status=self.status.value,
            status_detail=self.status_detail,
            status_code=self.status_code,
        )

    @staticmethod
    def from_dict(res: dict) -> 'Payment':
        return Payment(
            id=res['id'],
            method_id=res['method_id'],
            method_type=res['method_type'],
            creation_date=isoformat_to_timestamp(res['created_date']),
            approval_date=isoformat_to_timestamp(res['approved_date']),
            device_id=res['device_id'],
            status=PaymentStatus(res['status']),
            status_code=int(res['status_code']),
            status_detail=res['status_detail'],
        )


@dataclass
class CardPayment(Payment):
    card: CreditCard

    def to_dict(self) -> dict:
        return {**super().to_dict(), 'card': self.card.to_dict()}

    @staticmethod
    def from_dict(res: dict) -> 'CardPayment':
        payment = super().from_dict(res)
        return CardPayment(
            id=payment.id,
            method_id=payment.method_id,
            method_type=payment.method_type,
            creation_date=payment.creation_date,
            approval_date=payment.approval_date,
            device_id=payment.device_id,
            status=payment.status,
            status_code=payment.status_code,
            status_detail=payment.status_detail,
            card=res['card'].to_dict(),
        )
