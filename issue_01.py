import json
from keyword import iskeyword
from typing import Any, Dict


class Error(Exception):
    pass


class NotAllowedKeyError(Error):
    pass


class RequiredFieldError(Error):
    pass


class TooLowPriceError(Error):
    pass


class Advert:
    title: str
    price: int

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'

    def __init__(self, obj: Dict[str, Any], first_call: bool = True):
        for k, v in obj.items():
            if not k.isidentifier():
                raise NotAllowedKeyError(f'"{k}" is not valid identifier')
            if iskeyword(k):
                raise NotAllowedKeyError(f'"{k} is keyword"')

            if isinstance(v, dict):
                setattr(self, k, Advert(v, first_call=False))
                continue
            setattr(self, k, v)

        if first_call:
            self.price = obj.get('price', 0)

            if not hasattr(self, "title"):
                raise RequiredFieldError("Отсутствует поле title")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        if price < 0:
            raise TooLowPriceError(f'price {price} is too low')

        self._price = price


if __name__ == '__main__':
    data = """{
        "title": "python",
        "price": 5,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    advert = Advert(json.loads(data))

    print(advert)
    print(advert.location.address)
    print(advert.price)
