from enum import Enum
from typing import Optional
from dataclasses import dataclass
from dlocal.utils import optional_dict


class BankAccountType(Enum):
    CHECKING = 'CHECKING'
    SAVING = 'SAVING'


@dataclass
class BankTransfer:
    bank_account_type: BankAccountType
    bank_name: str
    bank_code: str
    beneficiary_name: str
    bank_account: str
    bank_account_label: str
    bank_account2: Optional[str]
    bank_account2_label: Optional[str]
    benficiary_document: str
    beneficiary_document_type: str
    reference: str
    redirect_url: str
    user_payment_amount: float
    payment_instruction: str

    def to_dict(self) -> dict:
        return optional_dict(
            bank_account_type=self.bank_account_type.value,
            bank_name=self.bank_name,
            bank_code=self.bank_code,
            beneficiary_name=self.beneficiary_name,
            bank_account=self.bank_account,
            bank_account2=self.bank_account2,
            bank_account_label=self.bank_account_label,
            bank_account2_label=self.bank_account2_label,
            benficiary_document=self.benficiary_document,
            beneficiary_document_type=self.beneficiary_document_type,
            reference=self.reference,
            redirect_url=self.redirect_url,
            user_payment_amount=self.user_payment_amount,
            payment_instruction=self.payment_instruction,
        )

    @staticmethod
    def from_dict(res: dict) -> 'BankTransfer':
        return BankTransfer(
            bank_account_type=BankAccountType(res['bank_account_type']),
            bank_name=res['bank_name'],
            bank_code=res['bank_code'],
            beneficiary_name=res['beneficiary_name'],
            bank_account=res['bank_account'],
            bank_account_label=res['bank_account_label'],
            bank_account2=res.get('bank_account2'),
            bank_account2_label=res.get('bank_account2_label'),
            benficiary_document=res['benficiary_document'],
            beneficiary_document_type=res['beneficiary_document_type'],
            reference=res['reference'],
            redirect_url=res['redirect_url'],
            user_payment_amount=res['user_payment_amount'],
            payment_instruction=res['payment_instruction'],
        )
