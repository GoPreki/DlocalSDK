from dataclasses import dataclass
from dlocal.utils import optional_dict


@dataclass
class Payer:
    name: str
    email: str
    phone: str
    document: str
    user_reference: str
    device_id: str
    ip: str

    def to_dict(self) -> dict:
        return optional_dict(
            name=self.name,
            email=self.email,
            phone=self.phone,
            document=self.document,
            user_reference=self.user_reference,
            device_id=self.device_id,
            ip=self.ip,
        )

    @staticmethod
    def from_dict(res: dict) -> 'Payer':
        return Payer(
            name=res['name'],
            email=res['email'],
            phone=res['phone'],
            document=res['document'],
            user_reference=res['user_reference'],
            device_id=res['device_id'],
            ip=res['ip'],
        )
