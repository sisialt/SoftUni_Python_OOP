from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
        except StopIteration:
            return None

        return product

    def remove(self, product_name: str):
        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
        except StopIteration:
            return None

        self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
