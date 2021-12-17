class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.name!r},{self.price!r}'

    def __str__(self):
        return f'Product: {self.name!r},{self.price!r}'


product = Product('car', 22232)
print(product)