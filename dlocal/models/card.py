from dataclasses import dataclass
from typing import Optional
from dlocal.utils import optional_dict


@dataclass
class PaymentCreditCard:
    save: bool
    card_id: Optional[str] = None
    token: Optional[str] = None
    installments: int = 1
    capture: bool = True

    def to_dict(self) -> dict:
        return optional_dict(
            card_id=self.card_id,
            token=self.token,
            save=self.save,
            installments=self.installments,
            capture=self.capture,
        )

    @staticmethod
    def from_dict(res: dict) -> 'PaymentCreditCard':
        return PaymentCreditCard(
            card_id=res['card_id'],
            token=res['token'],
            save=res['save'],
            installments=res['installments'],
            capture=res['capture'],
        )


@dataclass
class CreditCard:
    holder_name: str
    expiration_month: int
    expiration_year: int
    last4: str
    brand: str
    card_id: Optional[str]

    def to_dict(self) -> dict:
        return optional_dict(
            holder_name=self.holder_name,
            expiration_month=self.expiration_month,
            expiration_year=self.expiration_year,
            last4=self.last4,
            brand=self.brand,
            card_id=self.card_id,
        )

    @staticmethod
    def from_dict(res: dict) -> 'CreditCard':
        return CreditCard(
            holder_name=res['holder_name'],
            expiration_month=res['expiration_month'],
            expiration_year=res['expiration_year'],
            last4=res['last4'],
            brand=res['brand'],
            card_id=res.get('card_id'),
        )


@dataclass
class CardPayer:
    name: str
    document: str
    email: Optional[str] = None

    def to_dict(self) -> dict:
        return optional_dict(
            name=self.name,
            document=self.document,
            email=self.email,
        )

    @staticmethod
    def from_dict(res: dict) -> 'CardPayer':
        return CardPayer(
            name=res['name'],
            document=res['document'],
            email=res['email'],
        )
