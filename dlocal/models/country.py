from dataclasses import dataclass


@dataclass
class Country:
    code: str

    @staticmethod
    def get_country_by_name(name: str) -> 'Country':
        if name not in AVAILABLE_COUNTRIES:
            raise Exception('Country not supported')

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
    'México': Country(code='MX'),
    'Panamá': Country(code='PA'),
    'Paraguay': Country(code='PY'),
    'Perú': Country(code='PE'),
    'Uruguay': Country(code='UY'),
}
