from typing import Optional
from enum import Enum


class DlocalException(Exception):
    code: int
    message: str
    param: Optional[str]

    def __init__(self, code, message, param=None) -> None:
        self.code = code
        self.message = message
        self.param = param

        super().__init__(message)


class DlocalErrorCode(Enum):
    MISSING_INPUTS = 1
    MISSING_KEYS = 2
    INVALID_CREDENTIALS = 3001
    UNREGISTERED_IP_ADDRESS = 3002
    UNAUTHORIZED_MERCHANT = 3003
    PAYMENT_NOT_FOUND = 4000
    INVALID_REQUEST = 5000
    INVALID_PARAMETER = 5001
    INVALID_TRANSACTION_STATUS = 5002
    COUNTRY_NOT_SUPPORTED = 5003
    CURRENCY_NOT_ALLOWED = 5004
    UNAUTHORIZED_USER_CADASTRAL_SITUATION = 5005
    USER_LIMIT_EXCEEDED = 5006
    AMOUNT_EXCEEDED = 5007
    TOKEN_NOT_FOUND_OR_INACTIVE = 5008
    DUPLICATED_ORDER_ID = 5009
    UNAVAILABLE_METHOD = 5010
    OPERATION_NOT_SUPPORTED = 5013
    BLACKLISTED_USER = 5014
    CARD_REJECTED_BY_BANK = 5015
    AMOUNT_TOO_LOW = 5016
    INVALID_API_VERSION = 5017
    CHARGEBACK_IN_PLACE = 5018
    TOO_MANY_REQUESTS = 6000
    REQUEST_FAILED = 7000
