from enum import Enum
from typing import Optional
from dataclasses import dataclass
from dlocal.utils import optional_dict
from dlocal.utils.dates import isoformat_to_timestamp


class TicketType(Enum):
    NUMERIC = 'NUMERIC'
    BARCODE = 'BARCODE'
    CUSTOM = 'CUSTOM'
    REFERENCE_CODE = 'REFERENCE_CODE'


@dataclass
class Ticket:
    id: str
    type: TicketType
    number: Optional[str]
    barcode: Optional[str]
    format: Optional[str]
    expiration_date: float
    company_name: str
    company_id: str
    provider_name: str
    provider_logo: str
    image_url: str

    def to_dict(self) -> dict:
        return optional_dict(
            id=self.id,
            type=self.type.value,
            number=self.number,
            barcode=self.barcode,
            format=self.format,
            expiration_date=self.expiration_date,
            company_name=self.company_name,
            company_id=self.company_id,
            provider_name=self.provider_name,
            provider_logo=self.provider_logo,
            image_url=self.image_url,
        )

    @staticmethod
    def from_dict(res: dict) -> 'Ticket':
        return Ticket(
            id=res['id'],
            type=TicketType(res['type']),
            number=res.get('number'),
            barcode=res.get('barcode'),
            format=res.get('format'),
            expiration_date=isoformat_to_timestamp(res['expiration_date']),
            company_name=res['company_name'],
            company_id=res['company_id'],
            provider_name=res['provider_name'],
            provider_logo=res['provider_logo'],
            image_url=res['image_url'],
        )
