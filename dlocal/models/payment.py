from enum import Enum
from dataclasses import dataclass
from typing import Optional
from dlocal.models.bank_transfer import BankTransfer
from dlocal.models.card import CreditCard
from dlocal.models.cash import Ticket
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
    order_id: Optional[str]
    method_id: str
    method_type: str
    creation_date: float
    approval_date: Optional[float]
    status: PaymentStatus
    status_detail: str
    status_code: int

    def to_dict(self) -> dict:
        return optional_dict(
            id=self.id,
            orderd_id=self.order_id,
            payment_method_id=self.method_id,
            payment_method_type=self.method_type,
            created_date=self.creation_date,
            approved_date=self.approval_date,
            status=self.status.value,
            status_detail=self.status_detail,
            status_code=self.status_code,
        )

    @staticmethod
    def from_dict(res: dict) -> 'Payment':
        return Payment(
            id=res.get('id', res.get('payment_id')),
            order_id=res.get('order_id'),
            method_id=res.get('payment_method_id'),
            method_type=res.get('payment_method_type'),
            creation_date=isoformat_to_timestamp(res['created_date']),
            approval_date=isoformat_to_timestamp(res['approved_date']) if res.get('approved_date') else None,
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
        payment = Payment.from_dict(res)
        return CardPayment(
            id=payment.id,
            order_id=payment.order_id,
            method_id=payment.method_id,
            method_type=payment.method_type,
            creation_date=payment.creation_date,
            approval_date=payment.approval_date,
            status=payment.status,
            status_code=payment.status_code,
            status_detail=payment.status_detail,
            card=CreditCard.from_dict(res['card']),
        )


@dataclass
class RedirectPayment(Payment):
    redirect_url: Optional[str]

    def to_dict(self) -> dict:
        return {**super().to_dict(), 'redirect_url': self.redirect_url}

    @staticmethod
    def from_dict(res: dict) -> 'RedirectPayment':
        payment = Payment.from_dict(res)
        return RedirectPayment(
            id=payment.id,
            order_id=payment.order_id,
            method_id=payment.method_id,
            method_type=payment.method_type,
            creation_date=payment.creation_date,
            approval_date=payment.approval_date,
            status=payment.status,
            status_code=payment.status_code,
            status_detail=payment.status_detail,
            redirect_url=res.get('redirect_url'),
        )


@dataclass
class CashPayment(Payment):
    ticket: Optional[Ticket]

    def to_dict(self) -> dict:
        return {**super().to_dict(), 'ticket': self.ticket.to_dict() if self.ticket else None}

    @staticmethod
    def from_dict(res: dict) -> 'CashPayment':
        payment = Payment.from_dict(res)
        return CashPayment(
            id=payment.id,
            order_id=payment.order_id,
            method_id=payment.method_id,
            method_type=payment.method_type,
            creation_date=payment.creation_date,
            approval_date=payment.approval_date,
            status=payment.status,
            status_code=payment.status_code,
            status_detail=payment.status_detail,
            ticket=Ticket.from_dict(res['ticket']) if res.get('ticket') else None,
        )


@dataclass
class BankTransferPayment(Payment):
    bank_transfer: Optional[BankTransfer]

    def to_dict(self) -> dict:
        return {**super().to_dict(), 'bank_transfer': self.bank_transfer.to_dict() if self.bank_transfer else None}

    @staticmethod
    def from_dict(res: dict) -> 'BankTransferPayment':
        payment = Payment.from_dict(res)
        return BankTransferPayment(
            id=payment.id,
            order_id=payment.order_id,
            method_id=payment.method_id,
            method_type=payment.method_type,
            creation_date=payment.creation_date,
            approval_date=payment.approval_date,
            status=payment.status,
            status_code=payment.status_code,
            status_detail=payment.status_detail,
            bank_transfer=BankTransfer.from_dict(res['bank_transfer']) if res.get('bank_transfer') else None,
        )
