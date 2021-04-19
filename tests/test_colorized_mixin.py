from issue_02 import Advert


def test_corgi_in_colors(capfd):
    corgi = Advert({'title': 'Вельш-корги', 'price': 1000})
    assert '\x1b[1;33;40mВельш-корги | 1000 ₽' == repr(corgi)
