from dataclasses import dataclass
from dlocal.utils.exceptions import DlocalException, DlocalErrorCode


@dataclass
class Country:
    code: str

    @staticmethod
    def get_country_by_name(name: str) -> 'Country':
        if name not in AVAILABLE_COUNTRIES:
            raise DlocalException(message='Country not supported', code=DlocalErrorCode.COUNTRY_NOT_SUPPORTED.value)

        return AVAILABLE_COUNTRIES[name]


AVAILABLE_COUNTRIES = {
    'Argentina': Country(code='AR'),
    'Bolivia': Country(code='BO'),
    'Brasil': Country(code='BR'),
    'Chile': Country(code='CL'),
    'Colombia': Country(code='CO'),
    'Costa Rica': Country(code='CR'),
    'República Dominicana': Country(code='DO'),
    'Ecuador': Country(code='EC'),
    'El Salvador': Country(code='SV'),
    'Guatemala': Country(code='GT'),
    'Honduras': Country(code='HN'),
    'México': Country(code='MX'),
    'Nicaragua': Country(code='NI'),
    'Panamá': Country(code='PA'),
    'Paraguay': Country(code='PY'),
    'Perú': Country(code='PE'),
    'Uruguay': Country(code='UY'),
}
