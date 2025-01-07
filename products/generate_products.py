import random

from config.product_config import ProductsConfig
from config.product_config import ProductType

PERCENT_STUDIES = 0.20
PERCENT_COURSES = 0.40
PERCENT_WEBINARS = 0.40
PERCENT_FREE_WEBINARS = 0.20
PERCENT_INACTIVE_PRODUCTS = 0.10

class Product:
    def __init__(self, product_id, price, active, product_type, regular_discount):
        self.ProductID = product_id
        self.Price = price
        self.Active = active
        self.Type = product_type
        self.RegularDiscount = regular_discount


def generate_products():
    products = []
    ranges = ProductsConfig.get_products_ranges()

    for key, value in ranges.items():
        for i in range(value[0], value[1] + 1):
            price = random.randint(50, 500)

            if key == ProductType.WEBINAR:
                price = 0 if random.random() < PERCENT_FREE_WEBINARS else random.randint(50, 500)

            active = 1 if random.random() < PERCENT_INACTIVE_PRODUCTS else 0
            regular_discount = 0

            products.append(vars(Product(i, price, active, key.value, regular_discount)))

    return products
