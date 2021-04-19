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


class JsonObject:
    def __init__(self, obj: Dict[str, Any]):
        for k, v in obj.items():
            if not k.isidentifier():
                raise NotAllowedKeyError(f'"{k}" is not valid identifier')
            if iskeyword(k):
                raise NotAllowedKeyError(f'"{k} is keyword"')

            if isinstance(v, dict):
                setattr(self, k, JsonObject(v))
            else:
                setattr(self, k, v)


class Advert(JsonObject):
    title: str
    price: int

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'

    def __init__(self, obj: Dict[str, Any]):
        super().__init__(obj)

        if not hasattr(self, "title"):
            raise RequiredFieldError("Отсутствует поле title")
        if not hasattr(self, 'price'):
            self.price = 0

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
            },
        "yield": 123
        }"""
    advert = Advert(json.loads(data))

    print(advert)
    print(advert.location.address)
    print(advert.price)
    print(advert.foo)
