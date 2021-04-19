from issue_01 import Advert as OldAdvert

COLOR_GREEN = 32


class GreenColorMixin:
    title: str
    price: int
    template: str

    repr_color_code = COLOR_GREEN

    def __repr__(self):
        return f"\033[1;{self.repr_color_code};40m" + self.template.format(title=self.title, price=self.price)


class Advert(GreenColorMixin, OldAdvert):
    repr_color_code = 33
    template = '{title} | {price} ₽'


if __name__ == '__main__':
    oi_phone = Advert({"title": "oiPhone", "price": 100})
    print(oi_phone)
