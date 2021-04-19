from issue_02 import Advert


def test_corgi_in_colors(capfd):
    corgi = Advert({'title': 'Вельш-корги', 'price': 1000})
    corgi.coloring()
    print(corgi)
    out, _ = capfd.readouterr()
    assert '\x1b[1;33;40m\nВельш-корги | 1000 ₽\n' == out
