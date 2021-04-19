import pytest

from issue_01 import (
    NotAllowedKeyError,
    TooLowPriceError,
    Advert,
    RequiredFieldError
)


@pytest.mark.parametrize(
    'given, expect_error',
    [
        ({'*': ''}, NotAllowedKeyError),
        ({'yield': ''}, NotAllowedKeyError),
        ({'title': 'foo', 'price': -1}, TooLowPriceError),
        ({'price': 1}, RequiredFieldError),
    ]
)
def test_validation(given, expect_error):
    with pytest.raises(expect_error):
        Advert(given)


def test_default_price():
    advert = Advert({'title': 'foo'})
    assert advert.price == 0


def test_has_fields_from_dict():
    obj = {
        "title": "python",
        "price": 5,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
        }
    }
    advert = Advert(obj)

    assert advert.title == obj['title']
    assert advert.price == obj['price']
    assert advert.location.address == obj['location']['address']
    assert advert.location.metro_stations == obj['location']['metro_stations']
