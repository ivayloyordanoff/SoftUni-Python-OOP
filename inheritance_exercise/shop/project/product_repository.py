from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = None

        try:
            product = next(filter(lambda p: p.name == product_name, self.products))
        except StopIteration:
            pass

        if product:
            return product

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{product.name}: {product.quantity}" for product in self.products])
