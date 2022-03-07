from dataclasses import dataclass
from typing import Optional
from dlocal.utils import optional_dict


@dataclass
class CreditCard:
    holder_name: str
    expiration_month: int
    expiration_year: int
    last4: str
    brand: str
    card_id: str

    def to_dict(self) -> dict:
        return optional_dict(
            holder_name=self.holder_name,
            email=self.expiration_month,
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
            card_id=res['card_id'],
        )


@dataclass
class CardPayer:
    name: str
    document: str
    email: Optional[str]

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
