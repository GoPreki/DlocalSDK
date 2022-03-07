from enum import Enum


class PaymentMethodFlow(Enum):
    DIRECT = 'DIRECT'
    REDIRECT = 'REDIRECT'
