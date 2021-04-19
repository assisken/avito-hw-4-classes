from issue_01 import Advert as OldAdvert

COLOR_GREEN = 32


class ColorizeMixin:
    repr_color_code = COLOR_GREEN

    def coloring(self):
        print("\033[1;" + str(self.repr_color_code) + ";40m")


class Advert(OldAdvert, ColorizeMixin):
    repr_color_code = 33

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    oi_phone = Advert({"title": "oiPhone", "price": 100})
    oi_phone.coloring()
    print(oi_phone)
